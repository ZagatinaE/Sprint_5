from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsAll
from data import NAME,  INCORRECT_PASSWORD, NEW_EMAIL, NEW_PASSWORD


class TestStellarBurgers:
    def test_successful_registration(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.REGISTER_LINK).click()

        browser.find_element(*LocatorsAll.REGISTER_NAME).send_keys(NAME)
        browser.find_element(*LocatorsAll.REGISTER_EMAIL).send_keys(NEW_EMAIL)
        browser.find_element(*LocatorsAll.REGISTER_PASSWORD).send_keys(NEW_PASSWORD)
        browser.find_element(*LocatorsAll.REGISTER_BUTTON).click()

        assert (WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(LocatorsAll.HEADER_LOGIN)
        ))


    def test_invalid_password_registration(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.REGISTER_LINK).click()

        browser.find_element(*LocatorsAll.REGISTER_NAME).send_keys(NAME)
        browser.find_element(*LocatorsAll.REGISTER_EMAIL).send_keys(NEW_EMAIL)
        browser.find_element(*LocatorsAll.REGISTER_PASSWORD).send_keys(INCORRECT_PASSWORD)
        browser.find_element(*LocatorsAll.REGISTER_BUTTON).click()

        assert WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(LocatorsAll.PASSWORD_ERROR)
        ).text == "Некорректный пароль"










