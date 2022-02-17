from ...boundary.loginBoundary import loginBoundary
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class LoginTestCases(unittest.TestCase):
	def setUp(self):
		# Create boundary object
		self.boundary = loginBoundary()

		# Set up application settings
		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		
		# Set display of result differences to unlimited
		self.maxDiff = None

	#test if able to login with correct values
	def test_onSubmit_withCorrectValues(self):
		with self.app.test_request_context() as c:
			result = self.boundary.onSubmit('glen@hotmail.com', '123')
			expectedResult = 'Success'
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)
	
	#test if able to login with wrong values
	def test_onSubmit_withWrongValues(self):
		with self.app.test_request_context() as c:
			result = self.boundary.onSubmit('glen', '123456')
			expectedResult = 'Username or Password is incorrect'
			errorMessage = 'Incorrect values did not return Error'
			self.assertEqual(result, expectedResult, errorMessage)
	
	#test if able to display success function is able to redirect
	def test_displaySuccess_displaySuccessPage(self):
		with self.app.test_request_context() as c:
			result = self.boundary.displaySuccess().location
			expectedResult = redirect('/mainballot').location
			errorMessage = 'Failed to redirect to mainballot page'
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to display error function is able to redirect
	def test_displayError_displayErrorPage(self):
		with self.app.test_request_context() as c:
			result = self.boundary.displayError("Error").location
			expectedResult = redirect('/login').location
			errorMessage = "Username or Password is incorrect"
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()