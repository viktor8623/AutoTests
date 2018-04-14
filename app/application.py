from selenium import webdriver
import webium.settings
from app.session import SessionHelper
from actions.certificate import CertificateActions
from app.booking import BookingHelper


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
        webium.settings.wait_timeout = 5
        self.session = SessionHelper(self)
        # self.booking = BookingHelper(self)
        self.certificate = CertificateActions(self)


    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            return True
        except:
            return False

    def current_url(self):
        return self.driver.current_url
