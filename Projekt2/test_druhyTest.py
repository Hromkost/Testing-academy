import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False, slow_mo=3000
        )  
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_click_facebook_button(page):

    page.goto("https://cernyrytir.cz/")

    page.click('a[href="https://www.facebook.com/cernyrytircz/?fref=ts"]')

    page.click('span:has-text("Odmítnout volitelné soubory cookie")')