import time

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file_name


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        self.page.home.click_mine()
        self.page.mine.click_setting()

        if not self.page.mine.is_login():
            # 如果没有登录，那么直接登录
            self.page.mine.click_sign_up_and_login()
            self.page.sign_up_and_login.input_phone("18503080305")
            self.page.sign_up_and_login.input_password("123456")
            self.page.sign_up_and_login.click_login()

        # 填写收货地址
        self.page.mine.click_address()
        # 点击新建地址
        self.page.address_list.click_new_address()
        # 输入收货人
        self.page.address_info.input_name("hello")
        # 输入手机号
        self.page.address_info.input_mobile("18503080303")
        # 输入详细地址
        self.page.address_info.input_address("三单元")
        # 点击所在地区
        self.page.address_info.click_region()
        # 选择地区
        self.page.region.click_city_titles()
        # 点击确定
        self.page.region.click_commit()
        # 保存收货地址
        self.page.address_info.click_save_address()
        # 判断toast是不是"添加成功"
        assert self.page.address_info.is_toast_exist("添加成功")

        # if self.page.mine.is_login():
        #
        #     # 点击收货地址
        #     # 点击新增地址
        #     # 填写收货人
        # else:
        #     # 输入用户名
        #     # 输入密码
        #     # 点击登录
        #
        #     # 点击收货地址
        #     # 点击新增地址
        #     # 填写收货人