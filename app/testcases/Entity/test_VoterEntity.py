from pickle import TRUE
from ...entity.Voter import Voter
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class VoterTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = Voter("1")

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	# def test_get_email(self):
	# 	with self.app.test_request_context() as c:
	# 		result = self.entity.get_email()
	# 		expectedResult = "may@gmail.com"
	# 		errorMessage = 'Unable to retrieve voter email'
	# 		self.assertEqual(result, expectedResult, errorMessage)

	def test_insert_to_table(self):
		with self.app.test_request_context() as c:
			result = self.entity.insert_to_table("adfaadad","jackson@hotmail.com","1","fff")
			expectedResult = None
			errorMessage = 'Unable to insert voter'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_get_all_voters(self):
		with self.app.test_request_context() as c:
			result = self.entity.get_all_voters("1")
			expectedResult = [('may@gmail.com',), ('angeline@gmail.com',), ('jake@hotmail.com',)]
			errorMessage = 'Unable to get voter email for the project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_get_all_voters_id(self):
		with self.app.test_request_context() as c:
			result = self.entity.get_all_voters_id("1")
			expectedResult = [(1,), (2,), (3,)]
			errorMessage = 'Unable to get voters id for the project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_delete_allVoters(self):
		with self.app.test_request_context() as c:
			result = self.entity.delete_allVoters("2")
			expectedResult = None
			errorMessage = 'Unable to delete all voters for the project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_delete_child(self):
		with self.app.test_request_context() as c:
			result = self.entity.delete_child("7","3")
			expectedResult = None
			errorMessage = 'Unable to delete voter for the project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getVoterCount(self):
		with self.app.test_request_context() as c:
			result = self.entity.getVoterCount("1")
			expectedResult = 3
			errorMessage = 'Unable to count voters for the project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_get_all_voters_info(self):
		with self.app.test_request_context() as c:
			result = self.entity.get_all_voters_info("1")
			expectedResult = [('may@gmail.com', 'a12341'), ('angeline@gmail.com', 'bhsg12'), ('jake@hotmail.com', 'ajsh12')]
			errorMessage = 'Unable to retrieve voter info for the project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_checkVoterCredentials(self):
		with self.app.test_request_context() as c:
			result = self.entity.checkVoterCredentials("it99","123","4")
			expectedResult = True
			errorMessage = 'Failed to authenticate voters when credentials are valid'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getVoterID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getVoterID("it99","4")
			expectedResult = 9
			errorMessage = 'Unable to retrieve voter id'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_update_pw(self):
		with self.app.test_request_context() as c:
			result = self.entity.update_pw("it99","9@hotmail.com","4","1234")
			expectedResult = None
			errorMessage = 'Unable to update password for voter'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()