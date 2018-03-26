__author__ = 'urmi and minali'
# no change
import unittest
import LoginWrongCredentialsTest
import LoginCorrectCredentialsTest
import os
#import HTMLTestRunner

#direct = os.getcwd() + "\HTMLRunner"

class MyTestSuite(unittest.TestCase):

	def test_Issue1(self):
		login_test = unittest.TestSuite()
		login_test.addTests([
			unittest.defaultTestLoader.loadTestsFromTestCase(LoginCorrectCredentialsTest.LoginCorrect),
			#unittest.defaultTestLoader.loadTestsFromTestCase(LoginWrongCredentialsTest.LoginWrong),
		])

	def test_Issue2(self):
		login_test = unittest.TestSuite()
		login_test.addTests([
			#unittest.defaultTestLoader.loadTestsFromTestCase(LoginCorrectCredentialsTest.LoginCorrect),
			unittest.defaultTestLoader.loadTestsFromTestCase(LoginWrongCredentialsTest.LoginWrong),
		])

		# outfile = open("TestReport.html", "w")

		# runner1 = HTMLTestRunner.HTMLTestRunner(
		# 	stream=outfile,
		# 	title='Test Report',
		# 	description='Login Tests'
		# )

		# runner1.run(login_test)
		# outfile.close()





if __name__ == '__main__':
	unittest.main()
