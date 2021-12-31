from ..controllers.admin_viewQuestionsController import admin_viewQuestionsController
from flask import render_template, flash


class admin_viewQuestionsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = admin_viewQuestionsController()
		questionSet = controller.getQuestionsAndAnswers(projectID)

		return render_template('admin_viewQuestions.html', projectID=projectID, questionSet=questionSet)

	
	def displayError(self, projectID, error):
		flash(error)
		return self.displayPage(projectID)
