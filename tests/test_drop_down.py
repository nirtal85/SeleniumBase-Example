import allure
from pytest import mark
from selenium.webdriver.common.by import By

from pages.drop_down_page import DropDown
from pages.main_page import MainPage


class TestDropDown:

    @allure.description("Select first option in drop down")
    @mark.parametrize("option_index", [0, 1])
    def test_select_option_one(self, sb, option_index):
        sb.click_link_text(MainPage.drop_down)
        sb.assert_element_visible(DropDown.page_title, By.XPATH)
        sb.select_option_by_text(DropDown.drop_down, DropDown.options_text[option_index])
        sb.assert_text_visible(DropDown.options_text[option_index], DropDown.drop_down)
