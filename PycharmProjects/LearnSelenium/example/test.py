from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/97250/PycharmProjects/LearnSelenium/driver/chromedriver.exe')

driver.get('https://www.facebook.com/')

text = driver.find_element_by_link_text('שכחת את החשבון?')

text.click()

search = driver.find_element_by_id('identify_email')
search.clear()
search.send_keys('amitmizrahi231055@gmail.com')
search.send_keys(Keys.ENTER)