from pytest import mark

from pages.dynamic_controls_page import DynamicControls
from pages.main_page import MainPage


class TestDynamicControls:

    @mark.parametrize("action", ["remove", "add"])
    def test_remove_add_checkbox(self, sb, action):
        sb.click_link_text(MainPage.dynamic_controls)
        sb.assert_element_visible(DynamicControls.page_title)
        sb.click(DynamicControls.add_remove_checkbox_button)
        if action == "remove":
            sb.assert_element_not_visible(DynamicControls.check_box)
            sb.assert_text_visible("It's gone!", DynamicControls.success_message)
        elif action == "add":
            sb.assert_element_visible(DynamicControls.check_box)
            sb.assert_text_visible("It's back!", DynamicControls.success_message)

    @mark.parametrize("action", ["enable", "disable"])
    def test_enable_disable_text_field(self, action):
        self.click_link_text(MainPage.dynamic_controls)
        self.assert_element_visible(DynamicControls.page_title)
        self.click(DynamicControls.enable_disable_button)
        if action == "enable":
            disabled = self.find_element(DynamicControls.enable_disable_field).get_attribute("disabled")
            self.assert_true(disabled is None)
            self.assert_text_visible("It's enabled!", DynamicControls.success_message)
        elif action == "disable":
            disabled = self.find_element(DynamicControls.enable_disable_field).get_attribute("disabled")
            self.assert_true(disabled is not None)
            self.assert_text_visible("It's disabled!", DynamicControls.success_message)
