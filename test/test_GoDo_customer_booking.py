import pytest
from data.customer_booking import testdata


@pytest.mark.parametrize("tickets", testdata, ids=[repr(x) for x in testdata])
def test_purchasing_tickets(customer, tickets):
    """Order tickets via customer facing."""
    customer.customer.book_ticket(tickets)
