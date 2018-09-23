from page.home_page import HomePage
from page.mine_page import MinePage
from page.sign_up_and_login_page import SignUpAndLoginPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def sign_up_and_login(self):
        return SignUpAndLoginPage(self.driver)