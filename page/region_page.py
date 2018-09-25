import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class RegionPage(BaseAction):

    city_title_text_view = By.ID, "com.tpshop.malls:id/tv_city"

    # 确定
    commit_button = By.XPATH, "//*[@text='确定']"

    def click_city_title(self):
        cities = self.find_elements(self.city_title_text_view)
        index = random.randint(0, len(cities) - 1)
        cities[index].click()

    def click_city_titles(self):
        for i in range(4):
            self.click_city_title()
            time.sleep(1)

    def click_commit(self):
        self.click(self.commit_button)