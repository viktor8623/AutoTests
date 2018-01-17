import pytest
from data.add_certificate import testdata


@pytest.mark.parametrize("certificate", testdata, ids=[repr(x) for x in testdata])
def test_purchasing_certificate(app, certificate):
    app.add_new_certificate(certificate)
    app.check_if_it_created(certificate)
