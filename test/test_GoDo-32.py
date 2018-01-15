from model.certificate import Certificate



def test_purchasing_certificate_cash(app):
    app.certificate.navigate_to()
    app.certificate.select_certificate(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
                                                   first_tickets_type="3", second_tickets_type="3",
                                                   initial_amount="120.00", name_first_tickets_type="Adult",
                                                   name_second_tickets_type="Child"))
    app.certificate.charge_and_save("cash")        # only cash, check, card
    app.certificate.check_if_it_created(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
                                                   first_tickets_type="3", second_tickets_type="3",
                                                   initial_amount="120.00", name_first_tickets_type="Adult",
                                                   name_second_tickets_type="Child"))

def test_purchasing_certificate_credit_card(app):
    app.certificate.navigate_to()
    app.certificate.select_certificate(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
                                                   first_tickets_type="3", second_tickets_type="3",
                                                   initial_amount="120.00", name_first_tickets_type="Adult",
                                                   name_second_tickets_type="Child"))
    app.certificate.charge_and_save("card")        # only cash, check, card
    app.certificate.check_if_it_created(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
                                                   first_tickets_type="3", second_tickets_type="3",
                                                   initial_amount="120.00", name_first_tickets_type="Adult",
                                                   name_second_tickets_type="Child"))


def test_purchase_certificate_check(app):
    app.certificate.navigate_to()
    app.certificate.select_certificate(Certificate(type="Activity Tickets", activity="Beyond Good and Evil Tours",
                                                   second_tickets_type="1", initial_amount="20.00",
                                                   name_second_tickets_type="Child"))
    app.certificate.charge_and_save("check")       # only cash, check, card
    app.certificate.check_if_it_created(Certificate(type="Activity Tickets", activity="Beyond Good and Evil Tours",
                                                    second_tickets_type="1", initial_amount="20.00",
                                                    name_second_tickets_type="Child"))
