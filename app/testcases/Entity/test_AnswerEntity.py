from pickle import TRUE
from ...entity.Answer import Answer
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class AnswersTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = Answer()

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_insertVoterAnswer(self):
		with self.app.test_request_context() as c:
			result = self.entity.insertVoterAnswer("8","2","1")
			expectedResult = True
			errorMessage = 'User unable to vote'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_hasVoted(self):
		with self.app.test_request_context() as c:
			result = self.entity.hasVoted("7")
			expectedResult = True
			errorMessage = 'User has not voted'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getNumberOfUniqueVoter(self):
		with self.app.test_request_context() as c:
			result = self.entity.getNumberOfUniqueVoter("1")
			expectedResult = 3
			errorMessage = 'Number of voters in Project ID is wrong'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getVotes(self):
		with self.app.test_request_context() as c:
			result = self.entity.getVotes("1")
			expectedResult = [0, 0, 0, 0]
			errorMessage = 'Unable to get number of votes for candidate'
			self.assertEqual(result, expectedResult, errorMessage)


if __name__ == "__main__":
	unittest.main()