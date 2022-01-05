from flask import render_template, flash, redirect, url_for
from app.controllers.admin_editQuestionsController import admin_editQuestionsController
from app.entity.Candidates import Candidates
from app.entity.Questions import Questions
class admin_editQuestionsBoundary:
	def __init__(self):
		self.ERROR_NO_PERMISSION = "Not authorised to access this resource"

	def checkPermission(self, projectID, questionID):
		controller = admin_editQuestionsController()
		if questionID == "new_question":
			return True
		return controller.checkPermission(projectID, questionID)

	def displayPage(self, projectID, questionID):
		controller = admin_editQuestionsController()

		# Check if user has permission to save to this link
		if not self.checkPermission(projectID, questionID):
			return self.displayError(projectID, self.ERROR_NO_PERMISSION)
		
		projectName = controller.getProjectName(projectID)
		questionDetails = controller.getQuestion(questionID)
		candidateDetails = controller.getCandidates(questionID)

		return render_template('admin_editQuestions.html', projectID=projectID, 
														   projectName=projectName,
														   question=questionDetails,
														   candidates=candidateDetails)

	def addQuestion(self, projectID, question):
		controller = admin_editQuestionsController()
		questionID = controller.addQuestion(projectID, question)
		return self.displaySuccess(projectID)

	def saveQuestion(self, projectID, questionID, question):
		# Check if user has permission to save to this link
		if not self.checkPermission(projectID, questionID):
			return self.displayError(projectID, self.ERROR_NO_PERMISSION)

		# Create controller
		controller = admin_editQuestionsController()
		if controller.saveQuestion(projectID, questionID, question):
			return self.displaySuccess(projectID)
		return render_template(projectID, "Failed to update question")
	
	def deleteQuestion(self, projectID, questionID):
		# Check if user has permission to save to this link
		if not self.checkPermission(projectID, questionID):
			return self.displayError(projectID, self.ERROR_NO_PERMISSION)

		# Create Controllers	
		questions = Questions()
		candidates = Candidates()

		candidates.deleteCandidatesByQuestionID(projectID, questionID)
		questions.deleteQuestionByQuestionID(projectID, questionID)

		return self.displaySuccess(projectID)
	
	def displayError(self, projectID, error):
		flash(error)
		return redirect("../../{}/view_questions".format(projectID))
	
	def displaySuccess(self, projectID):
		return redirect("../../{}/view_questions".format(projectID))
	
	def redirect(self):
		pass

