from ..boundary.registrationBoundary import registrationBoundary
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class RegistrationTestCases(unittest.TestCase):
	def setUp(self):
		# Create boundary object
		self.boundary = registrationBoundary()

		# Set up application settings
		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		
		# Set display of result differences to unlimited
		self.maxDiff = None

	#test if able to login with invalid email format
	def test_onSubmit_withInvalidEmailFormat(self):
		with self.app.test_request_context() as c:
            # In this order: email,password,cfm_password,companyName,firstName,lastName 
			result = self.boundary.onSubmit('johnnyy.com','Aa12345678','Aa12345678','Voteforme Pte Ltd','Johnny','Tan')
			expectedResult = 'Email format is not valid'
			errorMessage = 'Email format is not valid'
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to login with incorrect password format
	def test_onSubmit_withInvalidPasswordFormat(self):
		with self.app.test_request_context() as c:
            # In this order: email,password,cfm_password,companyName,firstName,lastName 
			result = self.boundary.onSubmit('johnnyy123@hotmail.com','12345678','12345678','Voteforme Pte Ltd','Johnny','Tan')
			expectedResult = 'Password needs to contain at least 1 lowercase, 1 uppercase and 1 digit'
			errorMessage = 'Password format is invalid'
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to register with different passwords for password and confirm password 
	def test_onSubmit_withDifferentPassword(self):
		with self.app.test_request_context() as c:
            # In this order: email,password,cfm_password,companyName,firstName,lastName 
			result = self.boundary.onSubmit('johnnyy123@hotmail.com','Aa12345678','12345678','Voteforme','Johnny','Tan')
			expectedResult = 'Password fields do not match'
			errorMessage = 'Password fields do not match'
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to login with incorrect name format
	def test_onSubmit_withInvalidNameFormat(self):
		with self.app.test_request_context() as c:
            # In this order: email,password,cfm_password,companyName,firstName,lastName 
			result = self.boundary.onSubmit('johnnyy123@hotmail.com','Aa12345678','Aa12345678','Voteforme','123','123')
			expectedResult = 'Name contain invalid characters'
			errorMessage = 'Name is invalid'
			self.assertEqual(result, expectedResult, errorMessage)
	
	#test if able to display success function is able to redirect
	def test_displaySuccess_displaySuccessPage(self):
		with self.app.test_request_context() as c:
			result = self.boundary.displaySuccess().location
			expectedResult = redirect('/login').location
			errorMessage = 'Failed to redirect to login page'
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to display error function is able to redirect
	def test_displayError_displayErrorPage(self):
		with self.app.test_request_context() as c:
			result = self.boundary.displayError("Error").location
			expectedResult = redirect('/registration').location
			errorMessage = "Failed to redirect back to registration page"
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()