from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsAll



class TestStellarBurgersConstructor:
    def test_constructor_sections_navigation(self, browser):

        SECTIONS = {
            "Соусы": LocatorsAll.SAUCES_SECTION,
            "Начинки": LocatorsAll.FILLING_SECTION,
            "Булки": LocatorsAll.BUNS_SECTION
        }

        for section_name, section_locator in SECTIONS.items():
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(section_locator)
            ).click()

            assert (WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LocatorsAll.ACTIVE_SECTION)))