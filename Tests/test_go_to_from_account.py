from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsAll



class TestStellarBurgersGoTo:
    def test_return_to_constructor(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.CONSTRUCTOR_BUTTON).click()
        assert (WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(LocatorsAll.BUNS_SECTION)
        ))

    def test_return_via_logo(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.HEADER_LOGO).click()
        assert (WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(LocatorsAll.BUNS_SECTION)
        ))