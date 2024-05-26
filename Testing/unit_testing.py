import unittest
import app
import os
import sys

from pathlib import Path


# Get the absolute path of the project root directory
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))



class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Home Page', response.data)

    def test_login(self):
        response = self.app.post('/login', data=dict(
            username='testuser', password='testpass'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

    def test_signup(self):
        response = self.app.post('/signup', data=dict(
            username='newuser', password='newpass'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signup successful! Please log in.', response.data)

if __name__ == '__main__':
    unittest.main()
