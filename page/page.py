from page.address_info_page import AddressInfoPage
from page.address_list_page import AddressListPage
from page.home_page import HomePage
from page.mine_page import MinePage
from page.region_page import RegionPage
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

    @property
    def address_list(self):
        return AddressListPage(self.driver)

    @property
    def address_info(self):
        return AddressInfoPage(self.driver)

    @property
    def region(self):
        return RegionPage(self.driver)

