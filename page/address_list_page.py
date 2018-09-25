from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class AddressListPage(BaseAction):

    new_address_button = By.ID, "com.tpshop.malls:id/add_address_btn"

    def click_new_address(self):
        self.click(self.new_address_button)
