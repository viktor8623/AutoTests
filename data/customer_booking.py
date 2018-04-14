from model.tickets import Tickets


testdata = [

    Tickets(id_testdata="GoDo-394", customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            first_tickets_type="1", second_tickets_type="0", third_tickets_type=None, fourth_tickets_type=None,
            name_first_tickets_type="Adult", name_second_tickets_type="Child", year="2018", month="1", day="31",
            time="03:00 PM - 04:30 PM", first_name="Nicki", last_name="Minaj",
            phone="375290000000", email="test123@mail.com", zip_code="70050", promo_code=None, gift_certificate=None,
            card_number="4242424242424242", card_date="1020", card_cvc="303", card_zip="70050", ticket_total=None,
            booking_fee=None, discount=None, tax=None, grand_total=None),

    # GoDo-394 Customer-Facing booking flow. Сheck event time.



    Tickets(id_testdata="GoDo-1", customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=54b17f65-5032-4584-a32a-e2ec86120a71",
            first_tickets_type="1", second_tickets_type="2", third_tickets_type="1", fourth_tickets_type="3",
            name_first_tickets_type="Adult", name_second_tickets_type="Child", name_third_tickets_type="Retired",
            name_fourth_tickets_type="Winner of the competition",
            year="2018", month="1", day="21", time="05:20 PM - 08:20 PM", first_name="Nicki", last_name="Minaj",
            phone="375290000000", email="test123@mail.com", zip_code="70050", promo_code="5OFF", gift_certificate=None,
            card_number="4242424242424242", card_date="1020", card_cvc="303", card_zip="70050", ticket_total=None,
            booking_fee=None, discount=None, tax=None, grand_total=None)

    # GoDo-32 Purchasing certificate with number of tickets (120$, Check)
]