from pickle import TRUE
from ...entity.ProjectRoles import ProjectRoles
from flask import Flask, render_template, redirect, session, flash
import os

import unittest

class ProjectRolesTestCases(unittest.TestCase):
	def setUp(self):
		# Create entity object
		self.entity = ProjectRoles()

		template_dir = os.path.abspath('./app/template')
		static_dir = os.path.abspath('./app/static')
		self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
		self.app.secret_key="mykey123456"
		# Set display of result differences to unlimited
		self.maxDiff = None

	def test_getProjectsAsOwner(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjectsAsOwner("1")
			expectedResult = [1, 3, 4, 5, 6, 7, 8, 9]
			errorMessage = 'Unable to return all the Projects'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_checkUserHasOwnerRights(self):
		with self.app.test_request_context() as c:
			result = self.entity.checkUserHasOwnerRights("1", "1")
			expectedResult = True
			errorMessage = 'User does not have the right of this project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getProjectsAsVerifier(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjectsAsVerifier("2")
			expectedResult = [1]
			errorMessage = 'Unable to get Verifier roles'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getProjectDetails(self):
		with self.app.test_request_context() as c:
			result = self.entity.getProjectDetails("2")
			expectedResult = [(2, 2, 1, 'verifier', None, 1, 'Project Test A', 'DRAFT', '2022-01-08', '09:00', '2022-01-08', '12:00', 'aaaaaaaa'), (3, 2, 2, 'owner', None, 2, 'Project Test B', 'DRAFT', '2022-01-10', '11:00', '2022-01-11', '17:00', 'bbbbbbbb')]
			errorMessage = 'Unable to get Project details'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getVerifiersForProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.getVerifiersForProject("1")
			expectedResult = [{'recordID': 2, 'organizerID': 2, 'email': 'john@hotmail.com'}]
			errorMessage = 'Unable to get Verifiers for the Project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_addVerifier(self):
		with self.app.test_request_context() as c:
			result = self.entity.addVerifier("4","abcdefg@hotmail.com")
			expectedResult = True
			errorMessage = 'Unable to add verifier for the Project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_deleteVerifier(self):
		with self.app.test_request_context() as c:
			result = self.entity.deleteVerifier("1","4")
			expectedResult = True
			errorMessage = 'Unable to delete verifier for the Project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_addOwner(self):
		with self.app.test_request_context() as c:
			result = self.entity.addOwner("4","4")
			expectedResult = 13
			errorMessage = 'Unable to add owner for New Project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_setVerified(self):
		with self.app.test_request_context() as c:
			result = self.entity.setVerified("8","1")
			expectedResult = True
			errorMessage = 'Unable to set Project Approval to True'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_default_approval(self):
		with self.app.test_request_context() as c:
			result = self.entity.default_approval("8","1")
			expectedResult = True
			errorMessage = 'Unable to set Project Approval to False'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_allVerifierApprovedProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.allVerifierApprovedProject("1")
			expectedResult = False
			errorMessage = 'Result should be False as no verifier has approved the Project'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_get_organizer_info(self):
		with self.app.test_request_context() as c:
			result = self.entity.get_organizer_info("1")
			expectedResult = ('glen', 'lee', 'abs')
			errorMessage = 'Unable to retrieve organizer info'
			self.assertEqual(result, expectedResult, errorMessage)

	def test_getOwnersForProject(self):
		with self.app.test_request_context() as c:
			result = self.entity.getOwnersForProject("1")
			expectedResult = (1, 1, 'glen@hotmail.com')
			errorMessage = 'Unable to retrieve owner info'
			self.assertEqual(result, expectedResult, errorMessage)


if __name__ == "__main__":
	unittest.main()