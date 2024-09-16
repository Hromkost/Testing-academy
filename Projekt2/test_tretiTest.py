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

def test_search_buy(page):
    
    page.goto("https://cernyrytir.cz/")  
    
    page.fill('input[name="vyhledejkomplet"]', 'Duna')
    
    page.press('input[name="vyhledejkomplet"]', 'Enter')

    page.click("//*[contains(text(), 'Duna - Válka o Arrakis')]/ancestor::table//img[contains(@src, 'kosik.gif')]")

    assert "registracniudaje=1" in page.url
    
    
