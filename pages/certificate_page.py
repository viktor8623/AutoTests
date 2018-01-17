from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class CertificatePage:

    def __init__(self, driver):
        self.driver = driver


# Current Gift Certificates page.

    @property
    def add_new_certificate_button(self):
        return self.driver.find_element_by_css_selector("[ng-click='vm.openAddGiftCertificateModal();']")

    @property
    def first_row_name(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[2]").text

    @property
    def first_row_email(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[3]").text

    @property
    def first_row_initial_amount(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[4]").text

    @property
    def first_row_remain_amount(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[5]").text

    @property
    def first_row_purchase_date(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[6]").text

    @property
    def first_row_activity(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[7]").text

    @property
    def first_row_ticket_types(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[8]").text

    @property
    def first_row_quantity(self):
        return self.driver.find_element_by_xpath("//tbody/tr[1]/td[9]").text


# Add new certificate pop-up.


    @property
    def certificate_pop_up(self):
        return len(self.driver.find_elements_by_css_selector(".modal-content")) > 0

    def select_type(self, certificate_type):
        certificate_select = self.driver.find_element_by_id("type")
        Select(certificate_select).select_by_visible_text(certificate_type)

    @property
    def first_name_input(self):
        return self.driver.find_element_by_css_selector("#firstname")

    @property
    def last_name_input(self):
        return self.driver.find_element_by_css_selector("#lastname")

    @property
    def email_input(self):
        return self.driver.find_element_by_css_selector("#email")

    @property
    def initial_amount_input(self):
        return self.driver.find_element_by_id("initialamount")

    def select_activity(self, activity):
        if activity is not None:
            activity_list = self.driver.find_element_by_css_selector("#activity")
            Select(activity_list).select_by_visible_text(activity)

    @property
    def first_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@ng-if='vm.selectedType.key===3']/div[2]//input")

    @property
    def second_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@ng-if='vm.selectedType.key===3']/div[3]//input")

    @property
    def third_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@ng-if='vm.selectedType.key===3']/div[3]//input")

    def select_charge_type(self, charge_type):
        charge_type_list = self.driver.find_element_by_css_selector("#chargetype")
        Select(charge_type_list).select_by_visible_text(charge_type)

    @property
    def check_number_input(self):
        return self.driver.find_element_by_css_selector("#charge_checknumbner")

    @property
    def card_number_input(self):
        return self.driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]")

    @property
    def card_date_input(self):
        return self.driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]")

    @property
    def card_cvc_input(self):
        return self.driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]")

    @property
    def card_zip_input(self):
        return self.driver.find_element_by_xpath("//input[contains(@class, '__PrivateStripeElement-input')]")

    def click_save_button(self):
        self.driver.find_element_by_xpath("//button[contains(.,'Save')]").click()
        element = self.driver.find_element_by_css_selector(".modal-content")
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.staleness_of(element))

    def click_cancel_button(self):
        cancel_button = self.driver.find_element_by_xpath("//button[contains(.,'Cancel')]")
        cancel_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.staleness_of(cancel_button))
