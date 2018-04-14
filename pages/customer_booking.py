from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CustomerBookingPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, customer_URL):
        self.driver.get(customer_URL)

    # Step 1/5: Pick Tickets.

    @property
    def first_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][1]//input")

    @property
    def second_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][2]//input")

    @property
    def third_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][3]//input")

    @property
    def fourth_tickets_type_input(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][4]//input")

    # Titles under the pictures.

    @property
    def first_tickets_name(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][1]//div[@class='pill-box-left']/p").text

    @property
    def second_tickets_name(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][2]//div[@class='pill-box-left']/p").text

    @property
    def third_tickets_name(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][3]//div[@class='pill-box-left']/p").text

    @property
    def fourth_tickets_name(self):
        return self.driver.find_element_by_xpath("//div[@class='row'][4]//div[@class='pill-box-left']/p").text

    # Current tickets table.

    def wait_until_table_appear(self):
        table = self.driver.find_element_by_xpath("//div[@class='ticketDetails']")
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of(table))

    @property
    def current_tickets_first_row(self):
        return self.driver.find_element_by_xpath("//div[@class='ticketDetails']/p[1]").text

    @property
    def current_tickets_second_row(self):
        return self.driver.find_element_by_xpath("//div[@class='ticketDetails']/p[2]").text

    @property
    def current_tickets_third_row(self):
        return self.driver.find_element_by_xpath("//div[@class='ticketDetails']/p[3]").text

    @property
    def current_tickets_fourth_row(self):
        return self.driver.find_element_by_xpath("//div[@class='ticketDetails']/p[4]").text

    @property
    def next_button_1(self):
        return self.driver.find_element_by_xpath("//button[@id='ticketBookbtn']")

    # Step 2/5: Choose Date.

    def select_date(self, year, month, day):
        datepicker = self.driver.find_element_by_css_selector("#datepicker")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(datepicker))
        self.driver.find_element_by_xpath("//a[@class='ui-state-default']").click()
        # self.driver.find_element_by_xpath("//a[contains(@class, 'ui-state-default ui-state-hover')]").click()
        self.driver.execute_script("$('#datepicker').datepicker('setDate', new Date(%s, %s-1, %s));" % (year, month, day))

    @property
    def next_button_2(self):
        return self.driver.find_element_by_xpath("//button[@id='calenderbtn']")

    # Step 3/5: Choose Time.

    def pick_time_button(self, time):
        path = "//p[contains(.,'" + time + "')]/../../div[@class='timePill-right']/p"
        self.driver.find_element_by_xpath(path).click()

    def wait_until_button_3_clickable(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btneventSelect']")))

    @property
    def next_button_3(self):
        return self.driver.find_element_by_xpath("//button[@id='btneventSelect']")

    # Step 4/5: Your Info.

    @property
    def first_name_input(self):
        return self.driver.find_element_by_xpath("//input[@id='contactFirstName']")

    @property
    def last_name_input(self):
        return self.driver.find_element_by_xpath("//input[@id='contactLastName']")

    @property
    def phone_input(self):
        return self.driver.find_element_by_xpath("//input[@id='contactPhone']")

    @property
    def email_input(self):
        return self.driver.find_element_by_xpath("//input[@id='contactEmail']")

    @property
    def zip_input(self):
        return self.driver.find_element_by_xpath("//input[@id='contactZipCode']")

    @property
    def next_button_4(self):
        return self.driver.find_element_by_xpath("//button[@id='contactinforbtn']")

    # Final Step: Checkout

    @property
    def promo_code_input(self):
        return self.driver.find_element_by_xpath("//input[@id='discount_code']")

    @property
    def promo_code_button(self):
        return self.driver.find_element_by_xpath("//input[@id='discountBtnCode']")

    @property
    def gift_certificate_input(self):
        return self.driver.find_element_by_xpath("//input[@id='gift_certificate']")

    @property
    def gift_certificate_button(self):
        return self.driver.find_element_by_xpath("//input[@id='redeemBtnCode']")

    def switch_to_payment(self):
        payment = self.driver.find_element_by_xpath("//iframe[@name='__privateStripeFrame3']")
        self.driver.switch_to_frame(payment)

    def out_from_payment(self):
        self.driver.switch_to_default_content()

    @property
    def card_number_input(self):
        return self.driver.find_element_by_css_selector("input[name=cardnumber]")

    @property
    def card_date_input(self):
        return self.driver.find_element_by_css_selector("input[name=exp-date]")

    @property
    def card_cvc_input(self):
        return self.driver.find_element_by_css_selector("input[name=cvc]")

    @property
    def card_zip_input(self):
        return self.driver.find_element_by_css_selector("input[name=postal]")

    @property
    def next_button_5(self):
        return self.driver.find_element_by_xpath("//button[@class='btn btn-lg btn-blue']")

        # Information on the page.

    @property
    def checkout_activity(self):
        return self.driver.find_element_by_xpath("//div[@class='row lowBlue']//h2").text

    @property
    def checkout_date(self):
        return self.driver.find_element_by_xpath("//p[@class='tourDate']").text

    @property
    def checkout_time(self):
        return self.driver.find_element_by_xpath("//p[@class='tourTime']").text

    @property
    def checkout_first_tickets(self):
        return self.driver.find_element_by_xpath("//div[@id='tckTypes']/p[1]").text

    @property
    def checkout_second_tickets(self):
        return self.driver.find_element_by_xpath("//div[@id='tckTypes']/p[2]").text

    @property
    def checkout_third_tickets(self):
        return self.driver.find_element_by_xpath("//div[@id='tckTypes']/p[3]").text

    @property
    def checkout_fourth_tickets(self):
        return self.driver.find_element_by_xpath("//div[@id='tckTypes']/p[4]").text

    @property
    def tickets_cost(self):
        return self.driver.find_element_by_xpath("//div[@id='ticketbaseprice']").text

    @property
    def tax(self):
        return self.driver.find_element_by_xpath("//div[@id='taxesandfees']").text

    @property
    def total_price(self):
        return self.driver.find_element_by_xpath("//div[@id='tickettotalprice']").text

    # Summary Details.

    @property
    def customer_information(self):
        return self.driver.find_element_by_xpath("//div[@id='summarynamelbl']").text

    @property
    def zip_information(self):
        return self.driver.find_element_by_xpath("//div[@id='summaryAddresslbl']").text

    @property
    def phone_information(self):
        return self.driver.find_element_by_xpath("//div[@id='summaryPhonelbl']").text

    @property
    def email_information(self):
        return self.driver.find_element_by_xpath("//div[@id='summaryEmaillbl']").text

    @property
    def ticket_total(self):
        return self.driver.find_element_by_xpath("//div[@id='ticketTotallbl']").text

    @property
    def booking_fee(self):
        return self.driver.find_element_by_xpath("//div[@id='bookingFeeslbl']").text

    @property
    def discount(self):
        return self.driver.find_element_by_xpath("//div[@id='discountlbl']").text

    @property
    def tax(self):
        return self.driver.find_element_by_xpath("//div[@id='taxlbl']").text

    @property
    def grand_total(self):
        return self.driver.find_element_by_xpath("//div[@id='subTotallbl']").text
