import re,time
from playwright.sync_api import Page, expect


def test_case2(page: Page):
    page.goto("https://dodopizza.ru/")
    page.locator("text=Москва").nth(0).click()
    time.sleep(1)
    pizzas_table = page.locator("#pizzas")
    pizza_count = pizzas_table.locator(".sc-2v0umu-3").count()
    print(pizza_count)
    counter = 0
    summ = 0
    for i in range(pizza_count):
        if counter == 2:
            break

        print("Обработка "+str(i)+" случайной пиццы")
        pizza = pizzas_table.locator(".sc-2v0umu-3").nth(i)
        if pizza.locator(".sc-91ilwk-0.aUWsZ.product-control").is_visible() and pizza.locator(".sc-91ilwk-0.aUWsZ.product-control").inner_text()=="Выбрать":
            pizza.locator(".sc-91ilwk-0.aUWsZ.product-control").click()
            summ+= int(page.locator(".sc-15fdqut-18.lnqOCg .money__value").inner_text())
            page.locator(".sc-15fdqut-18.lnqOCg").locator("text=Добавить в корзину за ").click()
            counter+=1

    if counter<2:
        print("Not enough pizza to select " + str(counter))

    expect(page.locator(".ymp2tw-8.gtyfwx")).to_have_text("2")
    print("Successful check of amount")
    page.locator("text=Корзина").click()
    checking_value = ''.join(e for e in page.locator("div.sc-1uufjwy-0.cnlZaR > section > div.info > span").inner_text() if e.isalnum())
    print(page.locator("div.sc-1uufjwy-0.cnlZaR > section > div.info > span").inner_text())
    assert str(summ) in checking_value, "expected "+str(summ) + "got" + checking_value
    print("Successful check of amount")
    #expect(page.locator(".sc-1s1e6fo-0.bdrvPP .info")).to_have_text(re.compile(str(summ)))

    
    