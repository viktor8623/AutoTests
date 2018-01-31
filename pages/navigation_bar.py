from webium import BasePage, Find, Finds
from selenium.webdriver.common.by import By


class NavigationBar(BasePage):

    navigation_bar = Finds(by=By.XPATH, value="//ul[@class='nav navbar-nav navbar-right']")
    menu_drop_down = Find(by=By.XPATH, value="//a[contains(@class, 'dropdown-toggle waves-effect waves-light top-buttons-link')]")
    logout = Find(by=By.XPATH, value="//ul[contains(@class, 'dropdown-menu dropdown-menu-right')]/li[5]/a")
    main_actions_drop_down = Find(by=By.CSS_SELECTOR, value=".dropdown")
    sell_gift_certificates = Find(by=By.CSS_SELECTOR, value="[href = 'giftcertificate.aspx']")
