from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.driver import get_driver
import time


class CustomerBookingPage(BasePage):

    def __init__(self, **kwargs):
        super(CustomerBookingPage, self).__init__(**kwargs)

    # Step 1/5: Pick Tickets inputs.

    first_tickets_type_input = Find(by=By.XPATH, value="//div[@class='row'][1]//input")
    second_tickets_type_input = Find(by=By.XPATH, value="//div[@class='row'][2]//input")
    third_tickets_type_input = Find(by=By.XPATH, value="//div[@class='row'][3]//input")
    fourth_tickets_type_input = Find(by=By.XPATH, value="//div[@class='row'][4]//input")
    empty_space_first_page = Find(by=By.XPATH, value="//h4[text()='Step 1/5: Pick Tickets']")

    # Titles under the pictures.
    first_tickets_name = Find(by=By.XPATH, value="//div[@class='row'][1]//div[@class='pill-box-left']/p")
    second_tickets_name = Find(by=By.XPATH, value="//div[@class='row'][2]//div[@class='pill-box-left']/p")
    third_tickets_name = Find(by=By.XPATH, value="//div[@class='row'][3]//div[@class='pill-box-left']/p")
    fourth_tickets_name = Find(by=By.XPATH, value="//div[@class='row'][4]//div[@class='pill-box-left']/p")

    # Current tickets table.
    current_tickets_first_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[1]")
    current_tickets_second_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[2]")
    current_tickets_third_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[3]")
    current_tickets_fourth_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[4]")
    next_button_1 = Find(by=By.XPATH, value="//button[@id='ticketBookbtn']")

    # Step 2/5: Choose Date.

    datepicker = Find(by=By.XPATH, value="//table[@class='ui-datepicker-calendar']")
    next_button_2 = Find(by=By.XPATH, value="//button[@id='calenderbtn']")

    # Step 3/5: Choose Time.

    next_button_3 = Find(by=By.XPATH, value="//button[@id='btneventSelect']")

    # Step 4/5: Your Info.

    first_name_input = Find(by=By.XPATH, value="//input[@id='contactFirstName']")
    last_name_input = Find(by=By.XPATH, value="//input[@id='contactLastName']")
    phone_input = Find(by=By.XPATH, value="//input[@id='contactPhone']")
    email_input = Find(by=By.XPATH, value="//input[@id='contactEmail']")
    zip_input = Find(by=By.XPATH, value="//input[@id='contactZipCode']")
    next_button_4 = Find(by=By.XPATH, value="//button[@id='contactinforbtn']")

    # Final Step: Checkout

    promo_code_input = Find(by=By.XPATH, value="//input[@id='discount_code']")
    promo_code_button = Find(by=By.XPATH, value="//input[@id='discountBtnCode']")
    gift_certificate_input = Find(by=By.XPATH, value="//input[@id='gift_certificate']")
    gift_certificate_button = Find(by=By.XPATH, value="//input[@id='redeemBtnCode']")
    card_number_input = Find(by=By.XPATH, value="input[name=cardnumber]")
    card_date_input = Find(by=By.XPATH, value="input[name=exp-date]")
    card_cvc_input = Find(by=By.XPATH, value="input[name=cvc]")
    card_zip_input = Find(by=By.XPATH, value="input[name=postal]")
    next_button_5 = Find(by=By.XPATH, value="//button[@class='btn btn-lg btn-blue']")

    # Information on the page.

    checkout_activity = Find(by=By.XPATH, value="//div[@class='row lowBlue']//h2")
    checkout_date = Find(by=By.XPATH, value="//p[@class='tourDate']")
    checkout_time = Find(by=By.XPATH, value="//p[@class='tourTime']")
    checkout_first_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[1]")
    checkout_second_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[2]")
    checkout_third_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[3]")
    checkout_fourth_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[4]")
    tickets_cost = Find(by=By.XPATH, value="//div[@id='ticketbaseprice']")
    tax = Find(by=By.XPATH, value="//div[@id='taxesandfees']")
    total_price = Find(by=By.XPATH, value="//div[@id='tickettotalprice']")

    # Summary Details.

    customer_information = Find(by=By.XPATH, value="//div[@id='summarynamelbl']")
    zip_information = Find(by=By.XPATH, value="//div[@id='summaryAddresslbl']")
    phone_information = Find(by=By.XPATH, value="//div[@id='summaryPhonelbl']")
    email_information = Find(by=By.XPATH, value="//div[@id='summaryEmaillbl']")
    ticket_total = Find(by=By.XPATH, value="//div[@id='ticketTotallbl']")
    booking_fee = Find(by=By.XPATH, value="//div[@id='bookingFeeslbl']")
    discount = Find(by=By.XPATH, value="//div[@id='discountlbl']")
    tax_information = Find(by=By.XPATH, value="//div[@id='taxlbl']")
    grand_total = Find(by=By.XPATH, value="//div[@id='subTotallbl']")



if __name__ == '__main__':
    customer_page = CustomerBookingPage(url="https://dev.godo.io/customer_facing.aspx?Activity=b5382243-b660-451f-a2e0-c9a99dac7045")
    customer_page.open()
    customer_page.first_tickets_type_input.send_keys('1')
    customer_page.second_tickets_type_input.send_keys('2')
    time.sleep(10)
    get_driver().quit()












