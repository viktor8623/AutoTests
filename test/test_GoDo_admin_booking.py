import pytest
from data.tickets import testdata


@pytest.mark.parametrize("tickets", testdata, ids=[repr(x) for x in testdata])
def test_admin_booking(app, tickets):
    """Booking tickets via admin."""
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_booking()
    app.booking.refresh_page()

