
class SessionHelper:


    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        driver = self.app.driver
        driver.get("https://nfbooking.com/")

    def login(self, login, password):
        driver = self.app.driver
        self.open_login_page()
        driver.find_element_by_name("username").send_keys(login)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_css_selector("input[type=submit]").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[contains(@class, 'dropdown-toggle waves-effect waves-light top-buttons-link')]").click()
        driver.find_element_by_xpath("//ul[contains(@class, 'dropdown-menu dropdown-menu-right')]/li[5]/a").click()

