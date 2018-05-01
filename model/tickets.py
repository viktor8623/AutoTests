

class Tickets:

    def __init__(self, id_testdata=None, customer_URL=None, activity=None, first_tickets_type=None,
                 second_tickets_type=None, third_tickets_type=None, fourth_tickets_type=None,
                 name_first_tickets_type=None, name_second_tickets_type=None,
                 name_third_tickets_type=None, name_fourth_tickets_type=None, year=None, month=None, day=None,
                 time=None, first_name=None, last_name=None, phone=None, email=None, zip_code=None, promo_code=None,
                 gift_certificate_code=None, payment_type=None, saved_card=None,
                 card_number=None, card_date=None, card_cvc=None, card_zip=None, cash_recieved=None,
                 ticket_total=None, discount=None, gift_certificate=None, taxes=None, booking_fee=None,
                 grand_total=None):
        self.id_testdata = id_testdata
        self.customer_URL = customer_URL
        self.activity = activity
        self.first_tickets_type = first_tickets_type
        self.second_tickets_type = second_tickets_type
        self.third_tickets_type = third_tickets_type
        self.fourth_tickets_type = fourth_tickets_type
        self.name_first_tickets_type = name_first_tickets_type
        self.name_second_tickets_type = name_second_tickets_type
        self.name_third_tickets_type = name_third_tickets_type
        self.name_fourth_tickets_type = name_fourth_tickets_type
        self.year = year
        self.month = month
        self.day = day
        self.time = time
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.zip_code = zip_code
        self.promo_code = promo_code
        self.gift_certificate_code = gift_certificate_code
        self.payment_type = payment_type
        self.saved_card = saved_card
        self.card_number = card_number
        self.card_date = card_date
        self.card_cvc = card_cvc
        self.card_zip = card_zip
        self.cash_recieved = cash_recieved
        self.ticket_total = ticket_total
        self.discount = discount
        self.gift_certificate = gift_certificate
        self.taxes = taxes
        self.booking_fee = booking_fee
        self.grand_total = grand_total

    def __repr__(self):
        return "%s" % (self.id_testdata)
