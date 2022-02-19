from ..controllers.projectOwner_viewQuestionsController import projectOwner_viewQuestionsController
from flask import render_template, flash, session


class projectOwner_viewQuestionsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		controller = projectOwner_viewQuestionsController()
		projectName = controller.getProjectName(projectID)
		projectStatus = controller.getProjectStatus(projectID)
		questionSet = controller.getQuestionsAndAnswers(projectID)

		return render_template('organizer_viewQuestions.html', projectID=projectID, 
														  	   projectName=projectName,
															   projectStatus=projectStatus, 
														  	   questionSet=questionSet,
														  	   userType = session['userType'])

	
	def displayError(self, projectID, error):
		flash(error)
		return self.displayPage(projectID, userType=session['userType'])
