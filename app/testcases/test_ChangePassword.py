from ..boundary.organizer_changePasswordBoundary import organizer_changePasswordBoundary
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class changePasswordTestcases(unittest.TestCase):
	def setUp(self):
		# Create boundary object
		self.boundary = organizer_changePasswordBoundary()

		# Set up application settings
		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		
		# Set display of result differences to unlimited
		self.maxDiff = None

    #test if able to update password with wrong current/old password
	def test_onSubmitWithWrongCurrentPassword(self):
		with self.app.test_request_context() as c:
			session['user'] = '123@hotmail.com'
			result = self.boundary.onSubmit('123','Aa12345678','Aa12345678')
			expectedResult = "Old password is incorrect"
			errorMessage = 'Incorrect old password did not return error'
			self.assertEqual(result, expectedResult, errorMessage)

    #test if able to update password with unmatch New and confirm new password
	def test_onSubmitWithUnmatchPassword(self):
		with self.app.test_request_context() as c:
			session['user'] = '123@hotmail.com'
			result = self.boundary.onSubmit('Aa12345678','Bb33334444','Bb112222')
			expectedResult = "Password fields do not match"
			errorMessage = 'Incorrect old password did not return error'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()