from ...boundary.organizer_settingsBoundary import organizer_settingsBoundary
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class SettingsTestCases(unittest.TestCase):
	def setUp(self):
		# Create boundary object
		self.boundary = organizer_settingsBoundary()

		# Set up application settings
		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		
		# Set display of result differences to unlimited
		self.maxDiff = None

    #test if able to update details with correct values
	def test__onSubmit(self):
		with self.app.test_request_context() as c:
			session['user'] = 'abc@hotmail.com'
            #first_name,last_name,email,company_name
			result = self.boundary.onSubmit('danny','lim','123@hotmail.com','erd')
			expectedResult = "Success"
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

	def test__onSubmitWithWrongName(self):
		with self.app.test_request_context() as c:
			session['user'] = 'abc@hotmail.com'
            #first_name,last_name,email,company_name
			result = self.boundary.onSubmit('danny123','lim','123@hotmail.com','erd')
			expectedResult = "Name contain invalid characters"
			errorMessage = 'Incorrect values did not return Error'
			self.assertEqual(result, expectedResult, errorMessage)

	def test__onSubmitWithInvalidEmail(self):
		with self.app.test_request_context() as c:
			session['user'] = 'abc@hotmail.com'
            #first_name,last_name,email,company_name
			result = self.boundary.onSubmit('danny','lim','123hotmail.com','erd')
			expectedResult = "Email format is not valid"
			errorMessage = 'Incorrect values did not return Error'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()