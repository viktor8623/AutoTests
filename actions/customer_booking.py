from pages.customer_booking import CustomerBookingPage
from selenium.webdriver.common.keys import Keys
from time import sleep

class CustomerActions:

    def __init__(self, app):
        self.driver = app.driver
        self.booking = None

    def open_page(self, tickets):
        self.booking = CustomerBookingPage(driver=self.driver, url=tickets.customer_URL)
        self.booking.open()

    def select_tickets(self, tickets):
        if tickets.first_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.first_tickets_type_input.send_keys(tickets.first_tickets_type)
        if tickets.second_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.second_tickets_type_input.send_keys(tickets.second_tickets_type)
        if tickets.third_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.third_tickets_type_input.send_keys(tickets.third_tickets_type)
        if tickets.fourth_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.fourth_tickets_type_input.send_keys(tickets.fourth_tickets_type)
        self.booking.empty_space_first_page.click()
        self.booking.next_button_1.click()

    def select_date(self, tickets):
        # sleep(2)
        self.booking.datepicker.click()
        self.booking._driver.execute_script(
            "$('#datepicker').datepicker('setDate', new Date(%s, %s-1, %s))" % (tickets.year, tickets.month, tickets.day))
        # sleep(2)
        self.booking.next_button_2.click()
        sleep(5)


        time.sleep(10)
    #     self.select_tickets(tickets)
    #     self.verify_first_page(tickets)
    #     self.customer.next_button_1.click()
    #     self.customer.select_date(tickets.year, tickets.month, tickets.day)
    #     self.customer.next_button_2.click()
    #     self.customer.pick_time_button(tickets.time)
    #     self.customer.wait_until_button_3_clickable()
    #     self.customer.next_button_3.click()
    #     self.customer.first_name_input.send_keys(tickets.first_name)
    #     self.customer.last_name_input.send_keys(tickets.last_name)
    #     self.customer.phone_input.send_keys(tickets.phone)
    #     self.customer.email_input.send_keys(tickets.email)
    #     self.customer.zip_input.send_keys(tickets.zip_code)
    #     self.customer.email_input.click()
    #     self.customer.next_button_4.click()
    #     if tickets.promo_code is not None:
    #         self.customer.promo_code_input.send_keys(tickets.promo_code)
    #         self.customer.promo_code_button.click()
    #     if tickets.gift_certificate is not None:
    #         self.customer.gift_certificate_input.send_keys(tickets.gift_certificate)
    #         self.customer.gift_certificate_button.click()
    #     self.enter_payment_information(tickets)
    #     self.customer.next_button_5.click()
    #
    # def enter_payment_information(self, tickets):
    #     self.customer.switch_to_payment()
    #     self.customer.card_number_input.send_keys(tickets.card_number)
    #     self.customer.card_date_input.send_keys(tickets.card_date)
    #     self.customer.card_cvc_input.send_keys(tickets.card_cvc)
    #     self.customer.card_zip_input.send_keys(tickets.card_zip)
    #     self.customer.out_from_payment()
    #
    # def select_tickets(self, tickets):
    #     if tickets.first_tickets_type is not None and tickets.first_tickets_type != "0":
    #         self.customer.first_tickets_type_input.clear()
    #         self.customer.first_tickets_type_input.send_keys(tickets.first_tickets_type + Keys.ENTER)
    #     if tickets.second_tickets_type is not None and tickets.second_tickets_type != "0":
    #         self.customer.second_tickets_type_input.clear()
    #         self.customer.second_tickets_type_input.send_keys(tickets.second_tickets_type + Keys.ENTER)
    #     if tickets.third_tickets_type is not None and tickets.third_tickets_type != "0":
    #         self.customer.third_tickets_type_input.clear()
    #         self.customer.third_tickets_type_input.send_keys(tickets.third_tickets_type + Keys.ENTER)
    #     if tickets.fourth_tickets_type is not None and tickets.fourth_tickets_type != "0":
    #         self.customer.fourth_tickets_type_input.clear()
    #         self.customer.fourth_tickets_type_input.send_keys(tickets.fourth_tickets_type + Keys.ENTER)
    #
    #
    # def verify_first_page(self, tickets):
    #     assert self.customer.first_tickets_name == tickets.name_first_tickets_type, \
    #         "Wrong title under the first picture!"
    #     if tickets.name_second_tickets_type is not None:
    #         assert self.customer.second_tickets_name == tickets.name_second_tickets_type, \
    #             "Wrong title under the second picture!"
    #     if tickets.name_third_tickets_type is not None:
    #         assert self.customer.third_tickets_name == tickets.name_third_tickets_type, \
    #             "Wrong title under the third picture!"
    #     if tickets.name_fourth_tickets_type is not None:
    #         assert self.customer.fourth_tickets_name == tickets.name_fourth_tickets_type, \
    #             "Wrong title under the fourth picture!"
    #     self.customer.wait_until_table_appear()
    #     assert self.customer.current_tickets_first_row == str(tickets.first_tickets_type) + " " + tickets.name_first_tickets_type, \
    #         "Error in the first row in the current tickets table!"
    #     if tickets.name_second_tickets_type is not None:
    #         assert self.customer.current_tickets_second_row == str(tickets.second_tickets_type) + " " + tickets.name_second_tickets_type, \
    #         "Error in the second row in the current tickets table!"
    #     if tickets.name_third_tickets_type is not None:
    #         assert self.customer.current_tickets_third_row == str(tickets.third_tickets_type) + " " + tickets.name_third_tickets_type, \
    #         "Error in the third row in the current tickets table!"
    #     if tickets.name_fourth_tickets_type is not None:
    #         assert self.customer.current_tickets_fourth_row == str(tickets.fourth_tickets_type) + " " + tickets.name_fourth_tickets_type, \
    #         "Error in the fourth row in the current tickets table!"