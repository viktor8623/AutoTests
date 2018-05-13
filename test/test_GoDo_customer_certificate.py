import pytest
from data.certificates import testdata_cus1


@pytest.mark.parametrize("certificate", testdata_cus1, ids=[repr(x) for x in testdata_cus1])
def test_customer_booking(customer, certificate):
    """Purchasing gift certificates via customer facing with valid credit card."""
    customer.certificate.open_page(certificate)
    customer.certificate.fill_first_form(certificate)
    customer.certificate.verify_payment_info(certificate)
    customer.certificate.make_payment(certificate)
    customer.certificate.verify_summary_details(certificate)


@pytest.fixture
def stop():
    """Override admin's finalizer."""
    pass
