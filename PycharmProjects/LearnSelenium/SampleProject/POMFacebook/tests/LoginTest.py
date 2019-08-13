import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from SampleProject.POMFacebook.pages.LoginPage import LoginPage

twoMinWait = 2
chrome_driver_path = r'C:\Users\97250\PycharmProjects\LearnSelenium\driver\chromedriver.exe'
facebook_url = 'https://www.facebook.com/'
msg_error_invalid_username = 'הדוא"ל או מספר הטלפון שהזנת לא מתאימים לחשבון כלשהו. הירשם/הירשמי לחשבון.'
msg_error_invalid_password = 'הסיסמה שהזנת שגויה. שכחת את הסיסמה?'
msg_error_forgot_password = "אין תוצאות חיפוש\nהחיפוש שלך לא החזיר תוצאות. נסה/נסי שוב עם מידע אחר."
myEmail = input('Enter your email for facebook account: ')
myPassword = input('Enter your password for facebook account: ')
mere_email = 'rak'


class TestLoginPageFacebook(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path=chrome_driver_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_invalid_username(self):
        driver = self.driver
        driver.get(facebook_url)
        login = LoginPage(driver)

        login.login_button()
        msg_invalid_username = login.invalid_login_username()
        self.assertEqual(msg_invalid_username, msg_error_invalid_username)
        time.sleep(twoMinWait)

    def test_02_login_invalid_password(self):
        driver = self.driver
        driver.get(facebook_url)
        login = LoginPage(driver)

        login.enter_username(myEmail)
        login.login_button()
        msg_invalid_password = login.invalid_login_password()
        self.assertEqual(msg_invalid_password, msg_error_invalid_password)
        time.sleep(twoMinWait)

    def test_03_forgot_password(self):
        driver = self.driver
        driver.get(facebook_url)
        login = LoginPage(driver)

        login.forgot_password_button_click()
        time.sleep(twoMinWait)
        lstEmail = [myEmail, mere_email]
        for email in lstEmail:
            login.recoverUsername(email)
            login.search_button()
            time.sleep(twoMinWait)
            if email == myEmail:
                login.if_its_not_you_button()
                time.sleep(twoMinWait)
            elif email == mere_email:
                msg_invalid_search_email = login.invalid_search_email()
                self.assertEqual(msg_invalid_search_email, msg_error_forgot_password)

    def test_04_login_valid(self):
        driver = self.driver
        driver.get(facebook_url)
        login = LoginPage(driver)

        login.enter_username(myEmail)
        login.enter_password(myPassword)
        login.login_button()
        time.sleep(2)

        #login.setting_logout_account()
        #login.logout_button()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed!')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/97250/PycharmProjects/LearnSelenium/reports',
        report_title='Login attempt'))