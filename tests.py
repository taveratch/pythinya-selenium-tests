import unittest
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class TestAssertSeleniumTitle(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.email = 'adam.f@gmail.com'
        self.password = '12345678'
        print('Clearing all users in database')
        # requests.get('http://chinnnoo.xyz/api/admin/clear-users')

    def test1Signup(self):
        print('Testing sign up function')
        print('Opening the website')
        self.browser.get('http://pythinya.herokuapp.com')
        print('Checking the website\'s title')
        self.assertEqual("Pythinya", self.browser.title)
        print('Inserting user\' information')
        self.browser.find_element_by_id('signup-button').click()
        self.browser.find_element_by_id('firstname').send_keys('Adam')
        self.browser.find_element_by_id('lastname').send_keys('Family')
        self.browser.find_element_by_id('email').send_keys(self.email)
        self.browser.find_element_by_id('password').send_keys(self.password)
        self.browser.find_element_by_id('mobileNumber').send_keys('0834445555')
        time.sleep(2)
        print('Clicking the submit button')
        self.browser.find_element_by_id('submit-btn').click()
        time.sleep(5)
        print('Expect the current url to be signed in url')
        self.assertEqual('http://pythinya.herokuapp.com/client', self.browser.current_url)

    def signin(self):
        print('Opening the website')
        self.browser.get('http://pythinya.herokuapp.com')
        print('Checking the website\'s title')
        self.assertEqual("Pythinya", self.browser.title)
        print('Inserting user\'s credential')
        self.browser.find_element_by_id('signin-button').click()
        self.browser.find_element_by_id('email').send_keys(self.email)
        self.browser.find_element_by_id('password').send_keys(self.password)
        time.sleep(2)
        print('Clicking the submit button')
        self.browser.find_element_by_id('submit-btn').click()
        time.sleep(5)

    def test2Signin(self):
        print('Testing sign in function')
        self.signin()
        print('Expect the current url to be signed in url')
        self.assertEqual('http://pythinya.herokuapp.com/client', self.browser.current_url)

    def test3Signout(self):
        print('Testing sign out function')
        self.signin()
        print('Expect the current url to be signed in url')
        self.assertEqual('http://pythinya.herokuapp.com/client', self.browser.current_url)
        self.browser.find_element_by_id('signout-btn').click()
        time.sleep(10)
        print('Expect the current url to be index url')
        self.assertEqual('http://pythinya.herokuapp.com/', self.browser.current_url)
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
