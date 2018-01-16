import pytest
from data.add_certificate import testdata


@pytest.mark.parametrize("certificate", testdata, ids=[repr(x) for x in testdata])
def test_purchasing_certificate_cash(app, certificate):
    app.certificate.navigate_to()
    app.certificate.select_certificate(certificate)
    app.certificate.charge_and_save("cash")        # only cash, check, card
    app.certificate.check_if_it_created(certificate)


@pytest.mark.parametrize("certificate", testdata, ids=[repr(x) for x in testdata])
def test_purchasing_certificate_credit_card(app, certificate):
    app.certificate.navigate_to()
    app.certificate.select_certificate(certificate)
    app.certificate.charge_and_save("card")        # only cash, check, card
    app.certificate.check_if_it_created(certificate)


@pytest.mark.parametrize("certificate", testdata, ids=[repr(x) for x in testdata])
def test_purchase_certificate_check(app, certificate):
    app.certificate.navigate_to()
    app.certificate.select_certificate(certificate)
    app.certificate.charge_and_save("check")       # only cash, check, card
    app.certificate.check_if_it_created(certificate)
