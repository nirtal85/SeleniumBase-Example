from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.base_test import BaseTestCase
import allure


class TestLogIn(BaseTestCase):
    @allure.description("Login with valid credentials")
    def test_valid_login(self):
        self.click_link_text(MainPage.form_authentication)
        self.assert_element_visible(LoginPage.page_title)
        self.type(LoginPage.username_field, "tomsmith")
        self.type(LoginPage.password_field, "SuperSecretPassword!")
        self.click(LoginPage.login_button)
        self.assert_text_visible("You logged into a secure area!", LoginPage.message)

    @allure.description("Login with invalid credentials")
    def test_invalid_login(self):
        self.click_link_text(MainPage.form_authentication)
        self.assert_element_visible(LoginPage.page_title)
        self.type(LoginPage.username_field, "elias")
        self.type(LoginPage.password_field, "elias123")
        self.click(LoginPage.login_button)
        self.assert_text_visible("Your username is invalid!", LoginPage.message)
