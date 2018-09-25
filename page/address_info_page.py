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

    # 所在地区
    region_button = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    # 保存收货地址
    save_address_button = By.XPATH, "//*[@text='保存收货地址']"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_mobile(self, text):
        self.input(self.mobile_edit_text, text)

    def input_address(self, text):
        self.input(self.address_edit_text, text)

    def click_region(self):
        self.click(self.region_button)

    def click_save_address(self):
        self.click(self.save_address_button)


