from tests.base_test import BaseTestCase
from pages.add_remove_elements_page import AddRemoveElementsPage as addrem
from pages.main_page import MainPage
import allure


class TestAddRemoveElements(BaseTestCase):

    @allure.description("Add new element to page")
    def test_add_element(self):
        self.click(MainPage.add_remove_elements)
        self.assert_element(addrem.add_element_button)
        self.click(addrem.add_element_button)
        self.assert_element_visible(addrem.delete_added_elements_buttons_list)

    @allure.description("Delete an added element from page")
    def test_delete_element(self):
        self.click(MainPage.add_remove_elements)
        self.assert_element(addrem.add_element_button)
        self.click(addrem.add_element_button)
        self.click(addrem.delete_added_element)
        self.assert_element_not_visible(addrem.delete_added_element)
