from pages.navigation_bar import NavigationBar
from pages.certificate_page import CertificatePage
from datetime import datetime
import pytz


class CertificateActions:

    def __init__(self, driver):
        self.driver = driver
        self.certificate_page = CertificatePage(self.driver)
        self.navigation_bar = NavigationBar(self.driver)
        self.purchase_datetime = ""

    def add_new_certificate(self, cert):
        self.navigate_to()
        self.certificate_page.add_new_certificate_button.click()
        self.certificate_page.select_type(cert.certificate_type)
        self.certificate_page.first_name_input.send_keys(cert.first_name)
        self.certificate_page.last_name_input.send_keys(cert.last_name)
        self.certificate_page.email_input.send_keys(cert.email)
        self.enter_initial_amount(cert)
        self.select_activity_and_tickets(cert)
        self.check_initial_amout(cert)
        self.certificate_page.select_charge_type(cert.charge_type)
        self.enter_peyment_information(cert)
        self.certificate_page.click_save_button()
        self.get_purchase_datetime()

    def check_if_it_created(self, cert):
        assert self.certificate_page.first_row_name == cert.first_name + " " + cert.last_name, \
            "Wrong name in the table!"
        assert self.certificate_page.first_row_email == cert.email, "Wrong email in the table!"
        assert self.certificate_page.first_row_initial_amount == "$" + "{0:,.2f}".\
            format(float(cert.initial_amount)), "Wrong initial amount in the table!"
        assert self.certificate_page.first_row_remain_amount == "$" + "{0:,.2f}".format(float(cert.initial_amount)),\
            "Wrong remain amount in the table!"
        assert self.certificate_page.first_row_purchase_date == self.purchase_datetime,\
            "Wrong purchase date in the table!"
        if cert.certificate_type != "Specific Dollar Amount":
            assert self.certificate_page.first_row_activity == cert.activity, "Wrong activity in the table!"
        if cert.name_first_tickets_type is not None:
            assert cert.name_first_tickets_type in self.certificate_page.first_row_ticket_types,\
                "The first tickets type is not in the table!"
        if cert.name_second_tickets_type is not None:
            assert cert.name_second_tickets_type in self.certificate_page.first_row_ticket_types, \
                "The first tickets type is not in the table!"
        if cert.name_third_tickets_type is not None:
            assert cert.name_third_tickets_type in self.certificate_page.first_row_ticket_types, \
                "The first tickets type is not in the table!"
        # check for Tickets type field
        if cert.first_tickets_type is not None:
            assert cert.first_tickets_type in self.certificate_page.first_row_quantity, \
                "Wrong amount of first tickets in the table!"
        if cert.second_tickets_type is not None:
            assert cert.second_tickets_type in self.certificate_page.first_row_quantity, \
                "Wrong amount of second tickets in the table!"
        if cert.third_tickets_type is not None:
            assert cert.third_tickets_type in self.certificate_page.first_row_quantity, \
                "Wrong amount of third tickets in the table!"
        # check for Quantity field

    def get_purchase_datetime(self):
        self.purchase_datetime = datetime.now(tz=pytz.timezone('US/Central'))
        self.purchase_datetime = self.purchase_datetime.strftime('%m/%d/%Y %I:%M %p CT').lstrip("0").replace(" 0", " ")
        return self.purchase_datetime

    def enter_peyment_information(self, cert):
        if cert.charge_type == 'Credit Card':
            self.certificate_page.card_number_input.send_keys(cert.card_number)
            self.certificate_page.card_date_input.send_keys(cert.card_date)
            self.certificate_page.card_cvc_input.send_keys(cert.card_cvc)
            self.certificate_page.card_zip_input.send_keys(cert.card_zip)
        elif cert.charge_type == 'Check':
            self.certificate_page.check_number_input.send_keys(cert.check_number)
        else:
            pass

    def check_initial_amout(self, cert):
        if cert.certificate_type == "Activity Tickets":
            initial_amount = self.certificate_page.initial_amount_input.get_attribute("value")
            assert initial_amount == "%g" % float(
                cert.initial_amount), "Wrong value in the Initial Amount field!"
            # removing trailing zeros from a decimal part and comparing with expected result

    def select_activity_and_tickets(self, cert):
        if cert.activity is not None:
            self.certificate_page.select_activity(cert.activity)
            if cert.first_tickets_type is not None:
                self.certificate_page.first_tickets_type_input.send_keys(cert.first_tickets_type)
            if cert.second_tickets_type is not None:
                self.certificate_page.second_tickets_type_input.send_keys(cert.second_tickets_type)
            if cert.third_tickets_type is not None:
                self.certificate_page.third_tickets_type_input.send_keys(cert.third_tickets_type)

    def enter_initial_amount(self, cert):
        if cert.certificate_type == "Specific Dollar Amount" and cert.initial_amount is not None:
            self.certificate_page.initial_amount_input.clear()
            self.certificate_page.initial_amount_input.send_keys(cert.initial_amount)

    def navigate_to(self):
        self.driver.implicitly_wait(0.2)
        if self.navigation_bar.current_url() != "https://nfbooking.com/giftcertificate.aspx":
            self.navigation_bar.main_actions_drop_down.click()
            self.navigation_bar.sell_gift_certificates.click()
        elif self.certificate_page.certificate_pop_up is True:
            self.certificate_page.click_cancel_button()
        else:
            pass
        self.driver.implicitly_wait(15)
