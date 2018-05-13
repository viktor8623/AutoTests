import pytest
from data.certificates import testdata1


@pytest.mark.parametrize("certificate", testdata1, ids=[repr(x) for x in testdata1])
def test_purchasing_certificate(app, certificate):
    """Selling certificates via admin."""
    app.certificate.add_new_certificate(certificate)
    app.certificate.verify_created_certificate(certificate)
