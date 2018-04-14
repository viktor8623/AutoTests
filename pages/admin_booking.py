from webium import BasePage, Find, Finds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webium.wait import wait


class AdminBookingPage(BasePage):

    # First page.

    activity_list = Find(by=By.XPATH, value="//select[@id='activity'][@ng-model='vm.selectedActivity']")
    first_tickets_type = Find(by=By.XPATH, value="//tbody/tr[1]//input")
    second_tickets_type = Find(by=By.XPATH, value="//tbody/tr[2]//input")
    third_tickets_type = Find(by=By.XPATH, value="//tbody/tr[3]//input")
    fourth_tickets_type = Find(by=By.XPATH, value="//tbody/tr[4]//input")
    name_first_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[1]/td[1]")
    name_second_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[2]/td[1]")
    name_third_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[3]/td[1]")
    name_fourth_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[4]/td[1]")
    datepicker = Find(by=By.ID, value="datepicker_1")

