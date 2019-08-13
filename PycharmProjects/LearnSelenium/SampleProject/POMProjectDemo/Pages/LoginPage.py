from SampleProject.POMProjectDemo.Locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.invalidPassword_message_xpath = Locators.invalid_password_xpath
        self.remove_notification = Locators.turn_down_class_name

    def enter_username(self, username):
        username_textbox = self.driver.find_element_by_name(self.username_textbox_name)
        username_textbox.clear()
        username_textbox.send_keys(username)

    def enter_password(self, password, keys):
        password_textbox = self.driver.find_element_by_name(self.password_textbox_name)
        password_textbox.clear()
        password_textbox.send_keys(password)
        password_textbox.send_keys(keys)

    def check_invalid_password(self):
        error = self.driver.find_element_by_xpath(self.invalidPassword_message_xpath).text
        return error

    def remove_notification(self):
        remove_notification = self.driver.find_element_by_class_name(self.remove_notification)
        remove_notification.click()