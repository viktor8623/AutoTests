# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
#
# class BookingHelper():
#
#     def __init__(self, app):
#         self.app = app
#
#     def navigate_to(self):
#         driver = self.app.driver
#         if driver.current_url != "https://nfbooking.com/booking.aspx":
#             driver.find_element_by_css_selector(".dropdown").click()
#             driver.find_element_by_css_selector("[href='booking.aspx']").click()
#
#     def select_activity(self, type):
#         driver = self.app.driver
#         activity_list = driver.find_element_by_css_selector("[ng-model='sActivity.selectedActivity']")
#         Select(activity_list).select_by_visible_text(type)
#
#     def enter_fake_customer(self):
#         driver = self.app.driver
#         driver.find_element_by_link_text("Enter Fake Unique Customer").click()
#         driver.find_element_by_css_selector("[placeholder='Zip Code']").send_keys("70050")
#         driver.find_element_by_xpath("//button[text()='Select Tickets']").click()
#
#     def select_tickets(self, adult, child, senior):
#         driver = self.app.driver
#         WebDriverWait(driver, 10).until(EC.title_is("GoDo - Add/Edit Booking"))
#         driver.find_element_by_xpath("//tbody/tr[1]/td/input").send_keys(adult)
#         driver.find_element_by_xpath("//tbody/tr[2]/td/input").send_keys(child)
#         driver.find_element_by_xpath("//tbody/tr[3]/td/input").send_keys(senior)
#
#     def select_date_and_time(self, year, month, day, time):
#         driver = self.app.driver
#         datepicker = driver.find_element_by_css_selector("#datepicker")
#         wait = WebDriverWait(driver, 10)
#         wait.until(EC.visibility_of(datepicker))
#         driver.execute_script("$('#datepicker').datepicker('setDate', new Date(%s, %s-1, %s));" % (year, month, day))
#         time_list = driver.find_element_by_xpath("//select[@id='time']")
#         wait = WebDriverWait(driver, 15)
#         wait.until(EC.visibility_of(time_list))
#         Select(time_list).select_by_visible_text(time)
#
#     def click_complete_booking(self):
#         driver = self.app.driver
#         time.sleep(2)
#         complete_booking = driver.find_element(By.XPATH, "//button[text()='Complete Booking']")
#         # wait = WebDriverWait(driver, 10)
#         # wait.until(EC.element_to_be_clickable(complete_booking))
#         complete_booking.click()
#
#     def payment_by_cash(self, cash_received):
#         driver = self.app.driver
#         # WebDriverWait(driver, 30).until(EC.title_is("GoDo - Booking Charges"))
#         charge_list = driver.find_element_by_css_selector("#charge_type")
#         Select(charge_list).select_by_visible_text("Cash")
#
#         if cash_received == 'on':
#             driver.find_element_by_css_selector("#chargehtml_cashreceived").click()
#
#     def click_reserve_booking(self):
#         driver = self.app.driver
#         driver.find_element_by_xpath("//button[text()='Reserve Booking']").click()
#
