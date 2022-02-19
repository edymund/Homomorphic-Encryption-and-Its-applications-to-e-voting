from flask import render_template, flash, redirect, url_for, session
from app.controllers.organizer_editQuestionsController import organizer_editQuestionsController

class organizer_editQuestionsBoundary:
	def __init__(self):
		self.ERROR_NO_PERMISSION = "Not authorised to access this resource"

	def checkPermission(self, projectID, questionID):
		controller = organizer_editQuestionsController()
		if questionID == "new_question":
			return True
		return controller.checkPermission(projectID, questionID)

	def displayPage(self, projectID, questionID):
		controller = organizer_editQuestionsController()

		# Check if user has permission to save to this link
		if not self.checkPermission(projectID, questionID):
			return self.displayError(projectID, self.ERROR_NO_PERMISSION)
		
		projectName = controller.getProjectName(projectID)
		projectStatus = controller.getProjectStatus(projectID)
		questionDetails = controller.getQuestion(questionID)
		candidateDetails = controller.getCandidates(questionID)

		return render_template('organizer_editQuestions.html', projectID=projectID, 
														       projectName=projectName,
														       projectStatus=projectStatus,
														       questionID=questionID,
														       question=questionDetails,
														       candidates=candidateDetails,
														       userType=session['userType'])

	def addQuestion(self, projectID, question):
		controller = organizer_editQuestionsController()
		questionID = controller.addQuestion(projectID, question)
		return self.displaySuccess(projectID)

	def saveQuestion(self, projectID, questionID, question):
		# Check if user has permission to save to this link
		if not self.checkPermission(projectID, questionID):
			return self.displayError(projectID, self.ERROR_NO_PERMISSION)

		# Create controller
		controller = organizer_editQuestionsController()
		if controller.saveQuestion(projectID, questionID, question):
			return self.displaySuccess(projectID)
		return render_template(projectID, "Failed to update question")
	
	def deleteQuestion(self, projectID, questionID):
		# Check if user has permission to save to this link
		if not self.checkPermission(projectID, questionID):
			return self.displayError(projectID, self.ERROR_NO_PERMISSION)

		# Create Controllers
		controller = organizer_editQuestionsController()
		controller.deleteCandidatesByQuestionID(projectID, questionID)
		controller.deleteQuestionByQuestionID(projectID, questionID)

		return self.displaySuccess(projectID)
	
	def getProjectStatus(self,projectID):
		controller = organizer_editQuestionsController()
		return controller.getProjectStatus(projectID)
		
	def displayError(self, projectID, error):
		flash(error,'error')
		return redirect(f"../../{projectID}/view_questions")
	
	def displaySuccess(self, projectID):
		return redirect(f"../../{projectID}/view_questions")
	
	

