import re
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://dodopizza.ru/moscow")
    pizzas_table = page.locator("#pizzas")
    pizza_count = pizzas_table.locator(".sc-2v0umu-3").count()
    
    for i in range(pizza_count):
        pizza = pizzas_table.locator(".sc-2v0umu-3").nth(i)
        if pizza.locator(".sc-91ilwk-0.aUWsZ.product-control").is_visible() and pizza.locator(".sc-91ilwk-0.aUWsZ.product-control").inner_text()=="Выбрать":
            pizza.locator(".sc-91ilwk-0.aUWsZ.product-control").click()
            normal_size= int(page.locator(".sc-15fdqut-18.lnqOCg .money__value").inner_text())
            print("Selecting small pizza")
            page.locator(".sc-15fdqut-18.lnqOCg").locator("text=Маленькая")
            small_size= int(page.locator(".sc-15fdqut-18.lnqOCg .money__value").inner_text())
            assert(normal_size == small_size)
            page.locator(".sc-15fdqut-18.lnqOCg").locator("text=Добавить в корзину за ").click()
            break
    
    expect(page.locator(".ymp2tw-8.gtyfwx")).to_have_text("1")
    print("amount of pizza in cart is ")
    print(page.locator(".ymp2tw-8.gtyfwx").all_inner_texts())
