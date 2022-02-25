from pickle import TRUE
from ...entity.Candidates import Candidates
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class CandidatesTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = Candidates("1")

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getCandidateID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getCandidateID()
			expectedResult = 1
			errorMessage = 'Did not return correct Candidate ID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getProjectID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjectID()
			expectedResult = 1
			errorMessage = 'Did not return correct Project ID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getQuestionID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getQuestionID()
			expectedResult = 1
			errorMessage = 'Did not return correct Question ID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getOption(self):
		with self.app.test_request_context() as c:
			result = self.entity.getOption()
			expectedResult = "ID1_Q1C1"
			errorMessage = 'Did not return correct Candidate Option'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getImageFilename(self):
		with self.app.test_request_context() as c:
			result = self.entity.getImageFilename()
			expectedResult = "ID1_Q1C1.jpg"
			errorMessage = 'Did not return correct Image File'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getDescription(self):
		with self.app.test_request_context() as c:
			result = self.entity.getDescription()
			expectedResult = "Project ID 1 Question 1 Candidate 1"
			errorMessage = 'Did not return correct Description'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getCandidates(self):
		with self.app.test_request_context() as c:
			result = self.entity.getCandidates("1")
			expectedResult = [{'candidateID': 4, 'questionID': 2, 'candidateOption': 'ID1_Q2C4', 'imageFilename': 'ID1_Q2C4.jpg', 'description': 'Project ID 1 Question 2 Candidate 4'}, {'candidateID': 5, 'questionID': 2, 'candidateOption': 'ID1_Q2C5', 'imageFilename': None, 'description': 'Project ID 1 Question 2 Candidate 5'}, {'candidateID': 1, 'questionID': 1, 'candidateOption': 'ID1_Q1C1', 'imageFilename': 'ID1_Q1C1.jpg', 'description': 'Project ID 1 Question 1 Candidate 1'}, {'candidateID': 2, 'questionID': 1, 'candidateOption': 'ID1_Q1C2', 'imageFilename': 'ID1_Q1C2.jpg', 'description': 'Project ID 1 Question 1 Candidate 2'}, {'candidateID': 3, 'questionID': 1, 'candidateOption': 'ID1_Q1C3', 'imageFilename': None, 'description': None}]
			errorMessage = 'Did not return correct Candidates'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getCandidateDetails(self):
		with self.app.test_request_context() as c:
			result = self.entity.getCandidateDetails("1")
			expectedResult = {'candidateID': 1, 'questionID': 1, 'candidateOption': 'ID1_Q1C1', 'imageFilename': 'ID1_Q1C1.jpg', 'description': 'Project ID 1 Question 1 Candidate 1'}
			errorMessage = 'Did not return correct Candidates Details'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getCandidatesByQuestion(self):
		with self.app.test_request_context() as c:
			result = self.entity.getCandidatesByQuestion("1")
			expectedResult = [{'candidateID': 1, 'questionID': 1, 'candidateOption': 'ID1_Q1C1', 'imageFilename': 'ID1_Q1C1.jpg', 'description': 'Project ID 1 Question 1 Candidate 1'}, {'candidateID': 2, 'questionID': 1, 'candidateOption': 'ID1_Q1C2', 'imageFilename': 'ID1_Q1C2.jpg', 'description': 'Project ID 1 Question 1 Candidate 2'}, {'candidateID': 3, 'questionID': 1, 'candidateOption': 'ID1_Q1C3', 'imageFilename': None, 'description': None}]
			errorMessage = 'Did not return correct Candidates'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_deleteCandidatesByQuestionID(self):
		with self.app.test_request_context() as c:
			result = self.entity.deleteCandidatesByQuestionID("4","6")
			expectedResult = True
			errorMessage = 'Unable to delete candidates'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_deleteCandidateByCandidateID(self):
		with self.app.test_request_context() as c:
			result = self.entity.deleteCandidateByCandidateID("3","5","10")
			expectedResult = True
			errorMessage = 'Unable to delete candidates'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_checkExists(self):
		with self.app.test_request_context() as c:
			result = self.entity.checkExists("3","5","11")
			expectedResult = True
			errorMessage = 'Candidate does not exist'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_updateCandidate(self):
		with self.app.test_request_context() as c:
			result = self.entity.updateCandidate("11","UPDATE ID3_Q5C11","UPDATED Project ID 3 Question 5 Candidate 11","UPDATE_ID3_Q5C11.jpg")
			expectedResult = True
			errorMessage = 'Unable to update candidate'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_addNewCandidate(self):
		with self.app.test_request_context() as c:
			#projectID, questionID, candidateName, candidateDescription, filename
			result = self.entity.addNewCandidate("5","7","ID5_Q7","Project ID 5 Question 7","ID5_Q7.jpg")
			expectedResult = '14'
			errorMessage = 'Unable to add candidate'
			self.assertEqual(result, expectedResult, errorMessage)

if __name__ == "__main__":
	unittest.main()