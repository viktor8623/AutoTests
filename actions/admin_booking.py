from pages.navigation_bar import NavigationBar
from pages.admin_booking import AdminBookingPage


class AdminBooking:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.booking_page = AdminBookingPage(driver=self.driver)



