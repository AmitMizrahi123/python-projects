from SampleProject.POMFacebook.locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.email_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.button_login_id = Locators.button_login_id

        self.errorUsername_xpath = Locators.errorUsername_xpath
        self.errorPassword_xpath = Locators.errorPassword_xpath
        self.errorUsernameOrPassword_box_id = Locators.errorUsernameOrPassword_box_id

        self.forgot_password_linkText = Locators.forgot_password_linkText
        self.recoverUsername_email_id = Locators.recoverUsername_email_id
        self.search_button_name = Locators.search_button_name
        self.NoSearchForEmail_error_xpath = Locators.NoSearchForEmail_error_xpath
        self.ifItsNotYouButton_linkText = Locators.ifItsNotYouButton_linkText

        self.removeBlackScreen_className = Locators.removeBlackScreen_className
        self.setting_logout_account_id = Locators.setting_logout_account_id
        self.logoutAccount_button_linkText = Locators.logoutAccount_button_linkText

    def enter_username(self, username):
        username_textbox = self.driver.find_element_by_name(self.username_textbox_name)
        username_textbox.clear()
        username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = self.driver.find_element_by_name(self.password_textbox_name)
        password_textbox.clear()
        password_textbox.send_keys(password)

    def login_button(self):
        button = self.driver.find_element_by_id(self.button_login_id)
        button.click()

    def invalid_login_username(self):
        msg_error = self.driver.find_element_by_xpath(self.errorUsername_xpath).text
        return msg_error

    def invalid_login_password(self):
        msg_error = self.driver.find_element_by_xpath(self.errorPassword_xpath).text
        return msg_error

    def forgot_password_button_click(self):
        forgot_button = self.driver.find_element_by_link_text(self.forgot_password_linkText)
        forgot_button.click()

    def recoverUsername(self, email):
        recover_email = self.driver.find_element_by_id(self.recoverUsername_email_id)
        recover_email.clear()
        recover_email.send_keys(email)

    def search_button(self):
        button = self.driver.find_element_by_name(self.search_button_name)
        button.click()

    def if_its_not_you_button(self):
        not_you_button = self.driver.find_element_by_link_text(self.ifItsNotYouButton_linkText)
        not_you_button.click()

    def invalid_search_email(self):
        msg_error = self.driver.find_element_by_xpath(self.NoSearchForEmail_error_xpath).text
        return msg_error

    def remove_black_screen(self):
        black = self.driver.find_element_by_class_name(self.removeBlackScreen_className)
        black.click()

    def setting_logout_account(self):
        button_logout = self.driver.find_element_by_id(self.setting_logout_account_id)
        button_logout.click()

    def logout_button(self):
        exit_account = self.driver.find_element_by_link_text(self.logoutAccount_button_linkText)
        exit_account.click()
