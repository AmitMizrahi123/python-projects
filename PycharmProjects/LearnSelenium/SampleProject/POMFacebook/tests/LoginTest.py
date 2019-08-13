import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from SampleProject.POMFacebook.pages.LoginPage import LoginPage

chrome_driver_path = r'C:\Users\97250\PycharmProjects\LearnSelenium\driver\chromedriver.exe'


class TestLoginPageFacebook(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path=chrome_driver_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_invalid_username(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        login = LoginPage(driver)

        login.login_button()
        msg_invalid_username = login.invalid_login()
        self.assertEqual(msg_invalid_username, 'אישורים שגויים\nשם משתמש או סיסמה לא תקינים')
        time.sleep(2)

    def test_02_login_invalid_password(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        login = LoginPage(driver)

        login.enter_username('amitmizrahi231055@gmail.com')
        login.login_button()
        msg_invalid_password = login.invalid_login()
        self.assertEqual(msg_invalid_password, 'אישורים שגויים\nשם משתמש או סיסמה לא תקינים')
        time.sleep(2)

    def test_03_forgot_password(self):
        driver = self.driver
        driver.get('https://www.facebook.com')
        login = LoginPage(driver)

        login.forgot_password_button_click()
        time.sleep(2)
        lstEmail = ['amitmizrahi231055@gmail.com', 'rak']
        for email in lstEmail:
            login.recoverUsername(email)
            login.search_button()
            time.sleep(2)
            if email == 'amitmizrahi231055@gmail.com':
                login.ifItsNotYouButton()
            elif email == 'rak':
                msg_invalid_search_email = login.invalid_search_email()
                self.assertEqual(msg_invalid_search_email,
                                 "אין תוצאות חיפוש\nהחיפוש שלך לא החזיר תוצאות. נסה/נסי שוב עם מידע אחר.")
        time.sleep(2)

    def test_04_login_valid(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        login = LoginPage(driver)

        login.enter_username('amitmizrahi231055@gmail.com')
        login.enter_password('amitman231amk231')
        login.login_button()
        time.sleep(2)

        login.setting_logout_account()
        login.logout_button()

    @classmethod
    def tearDownClass(cls) -> None:
        #cls.driver.close()
        #cls.driver.quit()
        print('Test Completed!')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/97250/PycharmProjects/LearnSelenium/reports',
        report_title='Login attempt'))