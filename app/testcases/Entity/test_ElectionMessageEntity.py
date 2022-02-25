from pickle import TRUE
from ...entity.ElectionMessage import ElectionMessage
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class ElectionMessageTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = ElectionMessage("1")

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getElectionMsgsID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getElectionMsgsID()
			expectedResult = 1
			errorMessage = 'Unable to get Election Message ID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getProjID(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjID()
			expectedResult = 1
			errorMessage = 'Unable to get Project ID'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getPreMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.getPreMsg()
			expectedResult = "Do join us in this vote"
			errorMessage = 'Unable to get Pre Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getPostMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.getPostMsg()
			expectedResult = None
			errorMessage = 'Unable to get Post Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getInviteMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.getInviteMsg()
			expectedResult = "You are invited to vote"
			errorMessage = 'Unable to get Invitation Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getReminderMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.getReminderMsg()
			expectedResult = "Remember to vote"
			errorMessage = 'Unable to get Reminder Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setPreMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.setPreMsg("Come and join us in this Election!","3")
			expectedResult = None
			errorMessage = 'Unable to set Pre Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setPostMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.setPostMsg("Thank you for joining us in the Vote!","3")
			expectedResult = None
			errorMessage = 'Unable to set Post Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setInviteMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.setInviteMsg("You are invited to join us in this year Election!","3")
			expectedResult = None
			errorMessage = 'Unable to set Post Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setReminderMsg(self):
		with self.app.test_request_context() as c:
			result = self.entity.setReminderMsg("Please remember to give us your vote by 2 Feb 2023","3")
			expectedResult = None
			errorMessage = 'Unable to set Post Message'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_createNewRecord(self):
		with self.app.test_request_context() as c:
			result = self.entity.createNewRecord("3")
			expectedResult = 3
			errorMessage = 'Unable to create messages for Project'
			self.assertEqual(result, expectedResult, errorMessage)


if __name__ == "__main__":
	unittest.main()