__author__ = 'urmi and minali'

import uniest
impo LoginWrongCredentialsTest
import LoginCorrectCredentialsTest
import os

class MyTestSuite(unittest.TestCase):

	def test_login_correct_credential(self):
		unittest.defaultTestLoader.loadTestsFromTestCase(LoginCorrectCredentialsTest.LoginCorrect)

	def test_login_wrong_credential(self):
		unittest.defaultTestLoader.loadTestsFromTestCase(LoginWrongCredentialsTest.LoginWrong)


if __name__ == '__main__':
	unittest.main()
