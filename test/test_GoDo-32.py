from model.certificate import Certificate
import time



# def test_dead_of_night_tour(app):
#     """Purchasing certificate with number of tickets (120$, Check)"""
#     app.certificate.navigate_to()
#     app.certificate.select_certificate(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
#                                                    first_tickets_type="3", second_tickets_type="3",
#                                                    initial_amount="120.00"))
#     app.certificate.charge_and_save("card") # only cash, check, card
#     app.certificate.check_if_it_created(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
#                                                    first_tickets_type="3", second_tickets_type="3",
#                                                    initial_amount="120.00"))

# def test_beyound_good_and_evel_tours(app):
#     app.certificate.navigate_to()
#     app.certificate.select_certificate(Certificate(type="Activity Tickets", activity="Dead of Night Tour",
#                                                    first_tickets_type="3", second_tickets_type="3",
#                                                    initial_amount="120.00"))
#     app.certificate.charge_and_save("cash")  # only cash, check, card
#
def test_beyound_good_and_evel_tours2(app):
    app.certificate.navigate_to()
    app.certificate.select_certificate(Certificate(type="Activity Tickets", activity="Beyond Good and Evil Tours",
                                                   second_tickets_type="1"))
    app.certificate.charge_and_save("check")  # only cash, check, card
    app.certificate.check_if_it_created(Certificate(type="Activity Tickets", activity="Beyond Good and Evil Tours",
                                                    second_tickets_type="1", initial_amount="20.00"))
