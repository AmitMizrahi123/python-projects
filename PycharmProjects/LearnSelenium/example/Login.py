from selenium import webdriver
import time


class Login:
    def __init__(self, username, password):
        # browser settings
        self.driver = webdriver.Chrome(executable_path="C:/Users/97250/PycharmProjects/LearnSelenium/driver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # information login
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        driver.get('https://www.facebook.com')


if __name__ == '__main__':
    login = Login('amitmizrahi231055@gmail.com', 'amitman231amk231')
    login.login()