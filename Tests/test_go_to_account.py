from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsAll



class TestStellarBurgersAccount:

    def test_account_page_access(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        assert (WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(LocatorsAll.HEADER_LOGIN)
        ))