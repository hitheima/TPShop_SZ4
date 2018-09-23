from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.home.click_mine()
        self.page.mine.click_sign_up_and_login()
        # 输入用户名
        self.page.sign_up_and_login.input_phone("18503080305")
        # 输入密码
        self.page.sign_up_and_login.input_password("123456")
        # 点击登录
        self.page.sign_up_and_login.click_login()
        # 判断toast是否存在
        # if self.page.sign_up_and_login.is_toast_exits("登录成功"):
        #     assert True
        # else:
        #     assert False

        assert self.page.sign_up_and_login.is_toast_exits("登录成功")
