import allure
from pytest import mark
from selenium.webdriver.common.by import By

from pages.drop_down_page import DropDown
from pages.main_page import MainPage
from tests.base_test import BaseTestCase


class TestDropDown(BaseTestCase):

    @allure.description("Select first option in drop down")
    @mark.parametrize("option_index", [0, 1])
    def test_select_option_one(self, option_index):
        self.click_link_text(MainPage.drop_down)
        self.assert_element_visible(DropDown.page_title, By.XPATH)
        self.select_option_by_text(DropDown.drop_down, DropDown.options_text[option_index])
        self.assert_text_visible(DropDown.options_text[option_index], DropDown.drop_down)
