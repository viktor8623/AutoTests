import pytest
from data.tickets import testdata1


@pytest.mark.parametrize("tickets", testdata1, ids=[repr(x) for x in testdata1])
def test_purchasing_tickets(customer, tickets):
    """Order tickets via customer facing."""
    customer.booking.open_page(tickets)
    customer.booking.select_tickets(tickets)
    customer.booking.select_date(tickets)


