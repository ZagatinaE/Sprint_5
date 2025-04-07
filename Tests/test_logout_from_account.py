from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsAll
from data import CORRECT_PASSWORD, MY_EMAIL


class TestStellarBurgersLogout:
    def test_logout(self, browser):

        browser.find_element(*LocatorsAll.LOGIN_BUTTON).click()
        browser.find_element(*LocatorsAll.LOGIN_EMAIL_LOGIN).send_keys(MY_EMAIL)
        browser.find_element(*LocatorsAll.LOGIN_PASSWORD_LOGIN).send_keys(CORRECT_PASSWORD)
        browser.find_element(*LocatorsAll.LOGIN_BUTTON_LOGIN).click()
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(LocatorsAll.LOGOUT_BUTTON)
        ).click()

        assert (WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(LocatorsAll.LOGIN_BUTTON_LOGIN)
        ))