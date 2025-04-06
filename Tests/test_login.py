from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsAll
from data import CORRECT_PASSWORD, INCORRECT_PASSWORD, NEW_EMAIL, MY_EMAIL


class TestStellarBurgersLogin:


    def test_login_from_main_page(self, browser):
        browser.find_element(*LocatorsAll.LOGIN_BUTTON).click()
        browser.find_element(*LocatorsAll.LOGIN_EMAIL_LOGIN).send_keys(MY_EMAIL)
        browser.find_element(*LocatorsAll.LOGIN_PASSWORD_LOGIN).send_keys(CORRECT_PASSWORD)
        browser.find_element(*LocatorsAll.LOGIN_BUTTON_LOGIN).click()

        assert WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(LocatorsAll.MAKE_ORDER)
    )

    def test_login_from_account_button(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.LOGIN_EMAIL_LOGIN).send_keys(MY_EMAIL)
        browser.find_element(*LocatorsAll.LOGIN_PASSWORD_LOGIN).send_keys(CORRECT_PASSWORD)
        browser.find_element(*LocatorsAll.LOGIN_BUTTON_LOGIN).click()

        assert WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(LocatorsAll.MAKE_ORDER)
    )


    def test_login_from_register_form(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.REGISTER_LINK).click()
        browser.find_element(*LocatorsAll.LOGIN_LINK).click()

        browser.find_element(*LocatorsAll.LOGIN_EMAIL_LOGIN).send_keys(MY_EMAIL)
        browser.find_element(*LocatorsAll.LOGIN_PASSWORD_LOGIN).send_keys(CORRECT_PASSWORD)
        browser.find_element(*LocatorsAll.LOGIN_BUTTON_LOGIN).click()

        assert WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(LocatorsAll.MAKE_ORDER)
    )


    def test_login_from_password_recovery(self, browser):
        browser.find_element(*LocatorsAll.ACCOUNT_BUTTON).click()
        browser.find_element(*LocatorsAll.FORGOT_PASSWORD_LINK).click()
        browser.find_element(*LocatorsAll.LOGIN_BUTTON_FORGOT).click()

        browser.find_element(*LocatorsAll.LOGIN_EMAIL_LOGIN).send_keys(MY_EMAIL)
        browser.find_element(*LocatorsAll.LOGIN_PASSWORD_LOGIN).send_keys(CORRECT_PASSWORD)
        browser.find_element(*LocatorsAll.LOGIN_BUTTON_LOGIN).click()

        assert WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(LocatorsAll.MAKE_ORDER)
    )