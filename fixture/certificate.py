from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pytz


class CertificateHelper:

    def __init__(self, app):
        self.app = app

    def navigate_to(self):
        driver = self.app.driver
        driver.implicitly_wait(0.2)
        if driver.current_url != "https://nfbooking.com/giftcertificate.aspx":
            driver.find_element_by_css_selector(".dropdown").click()
            driver.find_element_by_css_selector("[href = 'giftcertificate.aspx']").click()
        elif len(driver.find_elements_by_css_selector(".modal-content")) > 0:
            cancel_button = driver.find_element_by_xpath("//button[contains(.,'Cancel')]")
            cancel_button.click()
            wait = WebDriverWait(driver, 10)
            wait.until(EC.staleness_of(cancel_button))
        else:
            pass
        driver.implicitly_wait(15)

    def select_certificate(self, cert):
        driver = self.app.driver
        driver.find_element_by_css_selector("[ng-click='vm.openAddGiftCertificateModal();']").click()
        # click add new certificate button
        certificate_type = driver.find_element_by_id("type")
        Select(certificate_type).select_by_visible_text(cert.type)
        # select ticket type: Specific Dollar Amount, Activity Tickets
        driver.find_element_by_css_selector("#firstname").send_keys(cert.first_name)
        driver.find_element_by_css_selector("#lastname").send_keys(cert.last_name)
        driver.find_element_by_css_selector("#email").send_keys(cert.email)
        if cert.type == "Specific Dollar Amount" and cert.initial_amount is not None:
            driver.find_element_by_id("initialamount").clear()
            driver.find_element_by_id("initialamount").send_keys(cert.initial_amount)
        if cert.activity is not None:
            activity_list = driver.find_element_by_css_selector("#activity")
            Select(activity_list).select_by_visible_text(cert.activity)
        # If type of the certificate is Activity Tickets select the activity.
        if cert.first_tickets_type is not None:
            driver.find_element_by_xpath("//div[@ng-if='vm.selectedType.key===3']/div[2]//input").send_keys(cert.first_tickets_type)
        if cert.second_tickets_type is not None:
            driver.find_element_by_xpath("//div[@ng-if='vm.selectedType.key===3']/div[3]//input").send_keys(cert.second_tickets_type)
        if cert.third_tickets_type is not None:
            driver.find_element_by_xpath("//div[@ng-if='vm.selectedType.key===3']/div[3]//input").send_keys(cert.third_tickets_type)
        # select tickets types
        if cert.type == "Activity Tickets":
            initial_amount = driver.find_element_by_id("initialamount").get_attribute("value")
            assert initial_amount == "%g" % float(cert.initial_amount), "Wrong value in the Initial Amount field!"
        # removing trailing zeros from a decimal part and comparing with expected result

    def charge_and_save(self, charge_type):   # only cash, check, card
        driver = self.app.driver
        charge_type_list = driver.find_element_by_css_selector("#chargetype")
        # select charge type
        if charge_type == 'cash':
            Select(charge_type_list).select_by_visible_text("Cash")
        elif charge_type == 'check':
            Select(charge_type_list).select_by_visible_text("Check")
            driver.find_element_by_css_selector("#charge_checknumbner").send_keys("123456")
        elif charge_type == 'card':
            Select(charge_type_list).select_by_visible_text("Credit Card")
            driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]").send_keys("4242424242424242")
            driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]").send_keys("1020")
            driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]").send_keys("303")
            driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]").send_keys("70050")
        else:
            print("\nYou entered the wrong charge_type!!!")
        # fill out the form with valid data
        driver.find_element_by_xpath("//button[contains(.,'Save')]").click()
        # click Save button
        element = driver.find_element_by_css_selector(".modal-content")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.staleness_of(element))
        # wait until the pop up is disappeared

    def check_if_it_created(self, cert):
        driver = self.app.driver
        purchase_datetime = datetime.now(tz=pytz.timezone('US/Central'))
        purchase_datetime = purchase_datetime.strftime('%m/%d/%Y %I:%M %p CT').lstrip("0").replace(" 0", " ")
        # request current server time immediately after ordering a certificate
        name = driver.find_element_by_xpath("//tbody/tr[1]/td[2]").text
        email = driver.find_element_by_xpath("//tbody/tr[1]/td[3]").text
        initial_amount = driver.find_element_by_xpath("//tbody/tr[1]/td[4]").text
        remain_amount = driver.find_element_by_xpath("//tbody/tr[1]/td[5]").text
        purchase_date = driver.find_element_by_xpath("//tbody/tr[1]/td[6]").text
        activity = driver.find_element_by_xpath("//tbody/tr[1]/td[7]").text
        ticket_types = driver.find_element_by_xpath("//tbody/tr[1]/td[8]").text
        quantity = driver.find_element_by_xpath("//tbody/tr[1]/td[9]").text
        # finds the text of the elements on the first row of the table on the certificate page
        assert name == cert.first_name + " " + cert.last_name, "Wrong name in the table!"
        assert email == cert.email, "Wrong email in the table!"
        assert initial_amount == "$" + "{0:,.2f}".format(float(cert.initial_amount)), "Wrong initial amount in the table!"
        assert remain_amount == "$" + "{0:,.2f}".format(float(cert.initial_amount)), "Wrong remain amount in the table!"
        assert purchase_date == purchase_datetime, "Wrong purchase date in the table!"
        if cert.type != "Specific Dollar Amount":
            assert activity == cert.activity, "Wrong activity in the table!"
        # compare expected result with actual result (data in the first row on the table)
        if cert.name_first_tickets_type is not None:
            assert cert.name_first_tickets_type in ticket_types, "The first tickets type is not in the table!"
        if cert.name_second_tickets_type is not None:
            assert cert.name_second_tickets_type in ticket_types, "The first tickets type is not in the table!"
        if cert.name_third_tickets_type is not None:
            assert cert.name_third_tickets_type in ticket_types, "The first tickets type is not in the table!"
        # check for Tickets type field
        if cert.first_tickets_type is not None:
            assert cert.first_tickets_type in quantity, "Wrong amount of first tickets in the table!"
        if cert.second_tickets_type is not None:
            assert cert.second_tickets_type in quantity, "Wrong amount of second tickets in the table!"
        if cert.third_tickets_type is not None:
            assert cert.third_tickets_type in quantity, "Wrong amount of third tickets in the table!"
        # check for Quantity field
