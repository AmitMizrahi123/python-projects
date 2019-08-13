import unittest, time, HtmlTestRunner
from selenium import webdriver
from SampleProject.POMProjectDemo.Pages.LoginPage import LoginPage
from selenium.webdriver.common.keys import Keys

# information about your log in
#username = input('Enter your username: ')
#password = input('Enter your password: ')

# friend that you want to give him likes
friend_like = input('Enter your friend name: ')


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\97250\PycharmProjects\LearnSelenium\driver\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

        # login to instagram
        login = LoginPage(driver)
        login.enter_username('zohary608@gmail.com')
        login.enter_password('MF4ever!', Keys.ENTER)
        time.sleep(2)

    def test_login_invalid_password(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

        # login to instagram
        login = LoginPage(driver)
        login.enter_username('asdkm')
        login.enter_password('asdasd', Keys.ENTER)
        time.sleep(2)

        # check if username is right
        msg_invalid_password = login.check_invalid_password()
        self.assertEqual(msg_invalid_password, "To secure your account, we've reset your password. Click "
                         + '"Forgot password?"' +
                         " on the login screen and follow the instructions to access your account.")

    def test_like_to_friend(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

        # login to instagram
        login = LoginPage(driver)
        login.enter_username('zohary608@gmail.com')
        login.enter_password('MF4ever!', Keys.ENTER)
        time.sleep(2)

        # likes time
        driver.get('https://www.instagram.com/' + friend_like)

    @classmethod
    def tearDownClass(cls) -> None:
        #cls.driver.close()
        #cls.driver.quit()
        print('Test completed!')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/97250/PycharmProjects/LearnSelenium/reports'))