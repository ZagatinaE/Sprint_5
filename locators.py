from selenium.webdriver.common.by import By

class LocatorsAll:
    #Главная страница:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']") #кнопка "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")#кнопка "Войти в аккаунт"
    # Разделы конструктора:
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")#раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")#раздел "Соусы"
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")# раздел "Начинки"
    MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")# кнопка "Оформить заказ"
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span") # раздел (булки,соусы,начинки) активен

    #Страница /login:
    LOGIN_EMAIL_LOGIN = (By.XPATH, "//input[@name='name']")#поле Email
    LOGIN_PASSWORD_LOGIN = (By.XPATH, "//input[@type='password']")#поле Пароль
    LOGIN_BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")#кнопка "Войти"
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]") #ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")#ссылка "Восстановить пароль"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]") #кнопка "Конструктор"
    HEADER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")#логотип Stellar Burgers
    HEADER_LOGIN = (By.XPATH, "//h2[contains(text(), 'Вход')]")  # заголовок "Вход"

    #Страница /register:
    REGISTER_NAME = (By.XPATH, "//fieldset[1]//input")#поле Имя
    REGISTER_EMAIL = (By.XPATH, "//fieldset[2]//input")#поле Email
    REGISTER_PASSWORD = (By.XPATH, "//input[@type='password']")#поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")#кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") #подсказка "Некорректный пароль"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") #кнопка "Войти"

    #Страница /forgot-password:
    LOGIN_BUTTON_FORGOT = (By.XPATH, "//a[contains(text(), 'Войти')]")#Кнопка "Войти"

    #Страница /profile
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")#Кнопка "Выход"


