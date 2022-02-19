from pickle import TRUE
from ...controllers.organizer_manageVerifiersController import organizer_manageVerifiersController
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class EditVerifierControllerTestCases(unittest.TestCase):
	def setUp(self):
		# Create boundary object
		self.controller = organizer_manageVerifiersController()

		# Set up application settings
		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getVerifier(self):
		with self.app.test_request_context() as c:
            #projectID, userID - admin ,email - verifier
			result = self.controller.getVerifier("1")
			expectedResult = [{'recordID': 2, 'organizerID': 2, 'email': 'john@hotmail.com'}, {'recordID': 12, 'organizerID': 4, 'email': 'abcdefg@hotmail.com'}]
			errorMessage = "Unable to retrieve Verifier"
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to continue voting if voted
	def test_addVerifier(self):
		with self.app.test_request_context() as c:
            #projectID, userID - admin ,email - verifier
			result = self.controller.addVerify("1","1","abcdefg@hotmail.com")
			expectedResult = True
			errorMessage = 'Unable to add verifier'
			self.assertEqual(result, expectedResult, errorMessage)

	#test if able to continue voting if voted
	def test_RemoveVerifier(self):
		with self.app.test_request_context() as c:
			result = self.controller.removeVerifier("1","1","4")
			expectedResult = True
			errorMessage = 'Unable to remove verifier'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()