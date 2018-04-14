

class Tickets:

    def __init__(self, id_testdata=None, customer_URL=None, first_tickets_type=None, second_tickets_type=None, third_tickets_type=None,
                 fourth_tickets_type=None, name_first_tickets_type=None, name_second_tickets_type=None,
                 name_third_tickets_type=None, name_fourth_tickets_type=None, year=None, month=None, day=None,
                 time=None, first_name=None, last_name=None, phone=None, email=None, zip_code=None, promo_code=None,
                 gift_certificate=None, card_number=None, card_date=None, card_cvc=None, card_zip=None,
                 ticket_total=None, booking_fee=None, discount=None, tax=None, grand_total=None):
        self.id_testdata = id_testdata
        self.customer_URL = customer_URL
        self.first_tickets_type = first_tickets_type
        self.second_tickets_type = second_tickets_type
        self.third_tickets_type = third_tickets_type
        self.fourth_tickets_type = fourth_tickets_type
        self.name_first_tickets_type = name_first_tickets_type
        self.name_second_tickets_type = name_second_tickets_type
        self.name_third_tickets_type = name_third_tickets_type
        self.name_fourth_tickets_type = name_fourth_tickets_type
        self.year =year
        self.month = month
        self.day = day
        self.time = time
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.zip_code = zip_code
        self.promo_code = promo_code
        self.gift_certificate = gift_certificate
        self.card_number = card_number
        self.card_date = card_date
        self.card_cvc = card_cvc
        self.card_zip = card_zip
        self.ticket_total = ticket_total
        self.booking_fee = booking_fee
        self.discount = discount
        self.tax = tax
        self.grand_total = grand_total

    def __repr__(self):
        return "%s" % (self.id_testdata)
