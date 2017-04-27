from pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, user, password):
        self.find_element_by_id('email').send_keys(user)
        self.find_element_by_id('password').send_keys(password)
        self.find_element_by_id('signin').click()