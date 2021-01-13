from selenium.webdriver.common.by import By

from pages.checkbox_page import CheckBox
from pages.main_page import MainPage
from tests.base_test import BaseTestCase
import allure


class TestCheckBox(BaseTestCase):

    @allure.description("Select an unchecked checkbox")
    def test_select_checkbox_1(self):
        self.click_link_text(MainPage.check_boxes)
        self.assert_element_visible(CheckBox.page_title, By.XPATH)
        checkbox_list = self.find_elements(CheckBox.checkboxes, By.CSS_SELECTOR)
        checkbox_list[0].click()
        self.assert_true(checkbox_list[0].is_selected())

    @allure.description("Un-select a checked checkbox")
    def test_un_select_checkbox_2(self):
        self.click_link_text(MainPage.check_boxes)
        self.assert_element_visible(CheckBox.page_title, By.XPATH)
        checkbox_list = self.find_elements(CheckBox.checkboxes)
        checkbox_list[1].click()
        self.assert_false(checkbox_list[1].is_selected())
