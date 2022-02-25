from pickle import TRUE
from ...entity.Questions import Questions
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class QuestionsTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = Questions("1")

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getQuestionsByProjectID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getQuestions("1")
			expectedResult = [{'questionID': 1, 'questionNo': 'Q1', 'question': 'Testcase for P.ID 1 Q1'}, {'questionID': 2, 'questionNo': 'Q2', 'question': 'Testcase for P.ID 1 Q2'}]
			errorMessage = 'Unable to get Questions'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getQuestionsByQuestionID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getQuestion("1")
			expectedResult = {'questionID': 1, 'questionNo': 'Q1', 'question': 'Testcase for P.ID 1 Q1'}
			errorMessage = 'Unable to get Questions'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_addQuestion(self):
		with self.app.test_request_context() as c:
			result = self.entity.addQuestion("7","Testcase for P.ID 7 Q2" )
			expectedResult = 2
			errorMessage = 'Unable to add Questions'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_updateQuestion(self):
		with self.app.test_request_context() as c:
			result = self.entity.updateQuestion("7","9","UPDATE Testcase for P.ID 7 Q1" )
			expectedResult = True
			errorMessage = 'Unable to update Question'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_checkQuestionIDBelongsToProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.checkQuestionIDBelongsToProject("9","7")
			expectedResult = True
			errorMessage = 'Question ID does not belong to project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_deleteQuestionByQuestionID(self):
		with self.app.test_request_context() as c:
			result = self.entity.deleteQuestionByQuestionID("9","11")
			expectedResult = True
			errorMessage = 'Unable to delete question'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()