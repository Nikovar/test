import re
from playwright.sync_api import Page, expect


def test_case0(page: Page):

    page.goto("https://dodopizza.ru/")
    #page.click("#react-app > nav > div > ul > li:nth-child(1) > a")
    #page.click(".sc-176km0j-0.iPVMjx.ymp2tw-5.kZstOz")
    page.locator("text=Москва").nth(0).click()
    page.click("text=Пицца")
    slogan = page.locator(".header__about-slogan")
    expect(slogan).to_have_text(re.compile("Доставка пиццы"))
    expect(slogan).to_have_text(re.compile("Москва"))
    print("Successful check that доставка пиццы near Москва")
    