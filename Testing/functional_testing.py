import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SafeMapTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Ensure that the ChromeDriver is in your PATH
        self.browser.get('http://127.0.0.1:8080')  # Make sure your Flask app is running on this URL

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.assertIn('Home', self.browser.title)

    def test_login_page(self):
        self.browser.get('http://127.0.0.1:8080/login')
        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')
        submit_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        username_input.send_keys('testuser')
        password_input.send_keys('testpass')
        submit_button.click()

        # Check for login success message
        success_message = self.browser.find_element(By.CLASS_NAME, 'flash-success')
        self.assertIn('Login successful!', success_message.text)

    def test_signup_page(self):
        self.browser.get('http://127.0.0.1:8080/signup')
        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')
        submit_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        username_input.send_keys('newuser')
        password_input.send_keys('newpass')
        submit_button.click()

        # Check for signup success message
        success_message = self.browser.find_element(By.CLASS_NAME, 'flash-success')
        self.assertIn('Signup successful! Please log in.', success_message.text)

if __name__ == '__main__':
    unittest.main()
