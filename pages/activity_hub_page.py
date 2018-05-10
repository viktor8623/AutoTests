from selenium.webdriver.common.by import By
from webium import BasePage, Find


class ActivityHubPage(BasePage):

    add_activity_button = Find(by=By.XPATH, value="//a[@href='activity_information.aspx']//h3[text()='Add Activities']")
