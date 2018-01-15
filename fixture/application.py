from selenium import webdriver
from fixture.session import SessionHelper
from fixture.certificate import CertificateHelper
from fixture.booking import BookingHelper

class Application:

    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.certificate = CertificateHelper(self)
        self.booking = BookingHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()