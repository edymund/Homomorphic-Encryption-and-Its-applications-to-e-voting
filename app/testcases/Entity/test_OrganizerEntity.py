from pickle import TRUE
from ...entity.Organizers import Organizers
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class OrganizersTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = Organizers("glen@hotmail.com")
		self.entity2 = Organizers("abc@hotmail.com")

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getOrganizerID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getOrganizerID()
			expectedResult = 1
			errorMessage = 'Correct values did not return OrganizerID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_VerifyLoginDetails(self):
		errorMsg = "Correct values provided, expected True but returned False"
		result = self.entity.verifyLoginDetails("glen@hotmail.com","123")
		self.assertTrue(result, errorMsg)

	def test_addNewUser(self):
		with self.app.test_request_context() as c:
			result = self.entity.addNewUser("test123@hotmail.com","123","abc","Adam","Tan")
			expectedResult = None
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_updatePassword(self):
		with self.app.test_request_context() as c:
			result = self.entity.updatePassword("123","Aa12345678")
			expectedResult = True
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_resetPassword(self):
		with self.app.test_request_context() as c:
			result = self.entity2.resetPassword("Aa12345678")
			expectedResult = True
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_updateDetails(self):
		with self.app.test_request_context() as c:
			result = self.entity2.updateDetails("Tammy","Lim","abc123@hotmail.com","abc")
			expectedResult = True
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_checkEmail(self):
		with self.app.test_request_context() as c:
			result = self.entity2.checkEmail("abc@hotmail.com")
			expectedResult = True
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getUserDetails(self):
		with self.app.test_request_context() as c:
			result = self.entity2.getUserDetails("abc@hotmail.com")
			expectedResult = [(3, 'abc@hotmail.com', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'abs', 'abc', 'abc')]
			errorMessage = 'Correct values did not return Success'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()