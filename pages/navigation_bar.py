

class NavigationBar:

    def __init__(self, driver):
        self.driver = driver

    @property
    def main_actions_drop_down(self):
        return self.driver.find_element_by_css_selector(".dropdown")

    @property
    def sell_gift_certificates(self):
        return self.driver.find_element_by_css_selector("[href = 'giftcertificate.aspx']")

    def current_url(self):
        return self.driver.current_url
