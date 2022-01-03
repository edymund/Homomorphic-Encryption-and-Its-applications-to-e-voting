from flask import render_template
from app.controllers.admin_editQuestionsController import admin_editQuestionsController
class admin_editQuestionsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID, questionID=None):
		controller = admin_editQuestionsController()
		
		projectName = controller.getProjectName(projectID)
		questionDetails = controller.getQuestion(questionID)
		candidateDetails = controller.getCandidates(questionID)

		return render_template('admin_editQuestions.html', projectID=projectID, 
														   projectName=projectName,
														   question=questionDetails,
														   candidates=candidateDetails)