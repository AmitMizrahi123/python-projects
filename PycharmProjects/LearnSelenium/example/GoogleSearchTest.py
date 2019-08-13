from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_google_amit(self):
        self.driver.get('https://www.google.co.il/')
        self.driver.find_element_by_name('q').send_keys('amit')
        self.driver.find_element_by_name('btnK').click()

    def test_search_google_automationstepbystep(self):
        self.driver.get('https://www.google.co.il/')
        self.driver.find_element_by_name('q').send_keys('Automation step by step')
        self.driver.find_element_by_name('btnK').click()

    def test_search_google_zohar(self):
        self.driver.get('https://www.google.co.il/')
        self.driver.find_element_by_name('q').send_keys('zohar')
        self.driver.find_element_by_name('btnK').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))