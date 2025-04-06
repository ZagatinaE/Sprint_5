import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By

@pytest.fixture (scope="function")
def browser():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get('https://stellarburgers.nomoreparties.site/')

    try:
        WebDriverWait(browser, 10).until(
            lambda b: "Stellar" in b.page_source
        )
    except:
        browser.quit()
        raise AssertionError("Страница не загрузилась за 5 секунд")

    yield browser
    browser.quit()





