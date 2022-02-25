from pickle import TRUE
from ...entity.Projectdetails import ProjectDetails
from flask import Flask, render_template, redirect, session, flash
import os
from datetime import datetime
import pytz

import unittest

class ProjectDetailsTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = ProjectDetails("1")
		self.entity2 = ProjectDetails("2")
		self.entity3 = ProjectDetails("8")  
		self.entity4 = ProjectDetails("9")      

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getProjectID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjectID()
			expectedResult = 1
			errorMessage = 'Unable to retrieve Project ID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getTitle(self):
		with self.app.test_request_context() as c:
			result = self.entity.getTitle()
			expectedResult = "Project Test A"
			errorMessage = 'Project ID did not return Project Title'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getStatus(self):
		with self.app.test_request_context() as c:
			result = self.entity.getStatus()
			expectedResult = "DRAFT"
			errorMessage = 'Project ID did not return Project Status'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getStartDate(self):
		with self.app.test_request_context() as c:
			result = self.entity.getStartDate()
			expectedResult = "2022-01-08"
			errorMessage = 'Project ID did not return Project Start Date'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getStartTime(self):
		with self.app.test_request_context() as c:
			result = self.entity.getStartTime()
			expectedResult = "09:00"
			errorMessage = 'Project ID did not return Project Start Time'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getEndDate(self):
		with self.app.test_request_context() as c:
			result = self.entity.getEndDate()
			expectedResult = "2022-01-08"
			errorMessage = 'Project ID did not return Project End Date'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getEndTime(self):
		with self.app.test_request_context() as c:
			result = self.entity.getEndTime()
			expectedResult = "12:00"
			errorMessage = 'Project ID did not return Project End Time'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getPublicKey(self):
		with self.app.test_request_context() as c:
			result = self.entity.getPublicKey()
			expectedResult = "aaaaaaaa"
			errorMessage = 'Project ID did not return Project Public Key'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_insertNewProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.insertNewProject()
			expectedResult = 11
			errorMessage = 'Unable to insert New Project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getProjectDetails(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjectDetails("1")
			expectedResult = {'id': 1, 'title': 'Project Test A', 'status':'DRAFT', 'startDateTime':'2022-01-08T09:00', 'endDateTime': '2022-01-08T12:00', 'publicKey': 'aaaaaaaa'}
			errorMessage = 'Unable to retrieve Project Details'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_updateProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.updateProject(3, "UPDATE Project Test C", "DRAFT", "2022-01-08", "09:00", "2022-01-08", "12:00", "UPDATE cccccccc")
			expectedResult = True
			errorMessage = 'Unable to update Project Details'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_deleteProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.deleteProject(10)
			expectedResult = True
			errorMessage = 'Unable to delete Project Details'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_isDraftMode(self):
		with self.app.test_request_context() as c:
			result = self.entity.isDraftMode(1)
			expectedResult = True
			errorMessage = 'Project is not in Draft Mode'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setStatusToPendingVerification(self):
		with self.app.test_request_context() as c:
			result = self.entity.setStatusToPendingVerification(3)
			expectedResult = True
			errorMessage = 'Project unable to set status to Pending Verification'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setStatusAsPublished(self):
		with self.app.test_request_context() as c:
			result = self.entity2.setStatusAsPublished(7)
			expectedResult = True
			errorMessage = 'Project unable to set status to PUBLISHED'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setStatusAsDraft(self):
		with self.app.test_request_context() as c:
			result = self.entity2.setStatusAsDraft(6)
			expectedResult = True
			errorMessage = 'Project unable to set status to DRAFT'
			self.assertEqual(result, expectedResult, errorMessage)


if __name__ == "__main__":
	unittest.main()