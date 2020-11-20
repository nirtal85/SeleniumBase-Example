from seleniumbase import BaseCase


class MainPage(BaseCase):
    _PAGE_TITLE = ".heading"
    _ADD_REMOVE_ELEMENTS = "[href='/add_remove_elements/']"
    _BASIC_AUTH = "[href='/basic_auth']"
    _CHALLENGING_DOM = "[href='/challenging_dom']"
    _CHECK_BOXES = "[href='/checkboxes']"
    _CONTEXT_MENU = "href='/context_menu']"
    _FORGOT_PASSWORD = "[href='/forgot_password']"
    _DROP_DOWN = "[href='/dropdown']"
    _DYNAMIC_CONTROLS = "[href='/dynamic_controls']"
    _FORM_AUTHENTICATION = "[href='/login']"
    _JAVASCRIPT_ALERTS = "[href='/javascript_alerts']"
    _KEY_PRESSES = "[href='/key_presses']"
    _NOTIFICATION_MESSAGE = "[href='/notification_message']"

    def click_add_remove_elements(self):
        self.click(self._ADD_REMOVE_ELEMENTS)

    
