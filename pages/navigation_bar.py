from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class NavigationBar(BasePage):

    navigation_bar = Finds(by=By.XPATH, value="//ul[@class='nav navbar-nav navbar-right']")
    time_tracker = Find(by=By.XPATH, value="//div[@class = 'switch-button-background']")
    time_tracker_checked = Find(by=By.XPATH, value="//div[@class = 'switch-button-background checked']")
    menu_drop_down = Find(by=By.XPATH, value="//a[contains(@class, 'dropdown-toggle waves-effect waves-light')]")
    logout = Find(by=By.XPATH, value="//ul/li/a[text()='Logout']")
    main_actions_drop_down = Find(by=By.CSS_SELECTOR, value=".dropdown")
    sell_gift_certificates = Find(by=By.CSS_SELECTOR, value="[href = 'giftcertificate.aspx']")
    add_a_booking = Find(by=By.XPATH, value="//*[@class='nav navbar-nav navbar-right']//a[text()='Add a Booking']")
    calendar = Find(by=By.XPATH, value="//li/a[@href='event_calendar.aspx']")
    profile_pic = Find(by=By.XPATH, value="//li[@class='dropdown top-menu-item-xs']//span/img")
    profile_pics = Finds(by=By.XPATH, value="//li[@class='dropdown top-menu-item-xs']//span/img")

    # Your Hubs navigation bar.

    sitemap = Find(by=By.XPATH, value="//i[@class='fa fa-sitemap']")
    activity_hub = Find(by=By.XPATH, value="//div[@class='side-bar right-bar nicescroll']//span[text()='Activity Hub']")
    marketing_hub = Find(by=By.XPATH, value="//li//span[text()='Marketing & Sales Hub']")
    people_hub = Find(by=By.XPATH, value="//li//span[text()='People Hub']")
