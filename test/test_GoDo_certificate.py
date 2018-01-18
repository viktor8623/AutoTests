import pytest
from data.add_certificate import testdata


@pytest.mark.parametrize("certificate", testdata, ids=[repr(x) for x in testdata])
def test_purchasing_certificate(app, certificate):
    """Selling certificates via admin."""
    app.certificate.add_new_certificate(certificate)
    app.certificate.check_if_it_created(certificate)
