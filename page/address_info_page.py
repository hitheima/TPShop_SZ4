from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class AddressInfoPage(BaseAction):

    # 收货人
    name_edit_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"

    # 手机号
    mobile_edit_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"

    #具体地址
    address_edit_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_mobile(self, text):
        self.input(self.mobile_edit_text, text)

    def input_address(self, text):
        self.input(self.address_edit_text, text)
