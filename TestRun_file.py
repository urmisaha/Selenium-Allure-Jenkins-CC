__author__ = 'urmi and minali'
# no change
import unittest
import LoginWrongCredentialsTest
import LoginCorrectCredentialsTest
import os

class MyTestSuite(unittest.TestCase):

	def test_login_correct_credential(self):
		unittest.defaultTestLoader.loadTestsFromTestCase(LoginCorrectCredentialsTest.LoginCorrect)
		# login_test = unittest.TestSuite()
		# login_test.addTests([
		# 	unittest.defaultTestLoader.loadTestsFromTestCase(LoginCorrectCredentialsTest.LoginCorrect),
		# ])

	def test_login_wrong_credential(self):
		login_test = unittest.TestSuite()
		login_test.addTests([
			unittest.defaultTestLoader.loadTestsFromTestCase(LoginWrongCredentialsTest.LoginWrong),
		])


if __name__ == '__main__':
	unittest.main()
