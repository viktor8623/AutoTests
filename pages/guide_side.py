from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement


class EventTicket(WebElement):
    day_slot_time = Finds(by=By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")


class GuidePage(BasePage):
    activity_name = Find(by=By.XPATH, value="//select[@id='activity_id']")
    hide_events = Find(by=By.XPATH, value="//input[@ng-model='calendar.hideEventsWithoutBooking']")
    date_picker = Find(by=By.XPATH, value="//i[@ng-model='calendar.customDate']")
    date_picker_next = Find(by=By.XPATH, value="//i[@class='glyphicon glyphicon-chevron-right']")
    day_button = Find(by=By.XPATH, value="//a[@ng-click='$event.preventDefault(); calendar.setDayView()']")
    day_date = Find(by=By.XPATH, value="//h3[@class='col-sm-5 col-md-4 cal_header ng-binding']")
    day_slots = Finds(EventTicket, By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")
    days_date_picker = Finds(by=By.XPATH, value="//span[@class='ng-binding']")
    time = Finds(by=By.XPATH, value="//div[@class='cal_event_tickets_avail ng-binding']")
    date_header = Find(by=By.XPATH, value="//span[@class='cal-header-text ng-binding']")
    time_slots = Finds(EventTicket, By.XPATH, value="//div[@class='col-sm-3 cal_event_time ng-binding']")
    close_button = Find(by=By.XPATH, value="//i[@class='close-x fa fa-times pull-right visible-md']")
    date_time_title = Find(by=By.XPATH, value="//span[@id='startTime']")
    activity_name_title = Find(by=By.XPATH, value="//span[@id='activityName']")
    check_in = Find(by=By.XPATH, value="//input[@data-checkincheckbox]")
    event_complete = Find(by=By.XPATH, value="//button[@id='markeventcomplete']")
    next_month = Find(by=By.XPATH, value="//button[@class='btn btn-default btn-sm pull-right uib-right']")
