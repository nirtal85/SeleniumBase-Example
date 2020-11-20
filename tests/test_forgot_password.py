from tests.base_test import BaseTestCase
from pages.main_page import MainPage
from pages.forgot_password import ForgotPassword
import allure


class TestForgotPassword(BaseTestCase):
    
    @allure.description("Send a passowrd reset email via forgot password")
    def test_forgot_password(self):
        self.click(MainPage.forgot_password)
        self.assert_element(ForgotPassword.retrieve_password_button)
        self.type(ForgotPassword.email_field, "some_email@gmail.com")
        self.click(ForgotPassword.retrieve_password_button)
        self.assert_element_visible(ForgotPassword.email_sent_message)
