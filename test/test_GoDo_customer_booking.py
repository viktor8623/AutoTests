import pytest
from data.tickets import testdata


@pytest.mark.parametrize("tickets", testdata, ids=[repr(x) for x in testdata])
def test_purchasing_tickets(customer, tickets):
    """Order tickets via customer facing."""
    customer.booking.(tickets)
