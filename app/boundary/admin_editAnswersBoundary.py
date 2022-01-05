from ..controllers.admin_editAnswersController import admin_editAnswersController
from flask import render_template, flash, redirect

class admin_editAnswersBoundary:
	def __init__(self):
		pass

	def hasPermission(self, projectID, questionID, candidateID):
		controller = admin_editAnswersController()
		return controller.checkPermission(projectID, questionID, candidateID)

		
	def displayPage(self, projectID, questionID, candidateID):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError()

		controller = admin_editAnswersController()
		projectName = controller.getProjectName(projectID)
		candidateDetails = controller.getCandidateDetails(candidateID)

		return render_template('admin_editAnswers.html', projectName=projectName, candidate=candidateDetails)
	
	def updateCandidate(self, projectID, questionID, candidateID, candidateName, candidateDescription, filename):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError()
		
		controller = admin_editAnswersController()
		# existingFilename = controller.getCandidateDetails(candidateID)["imageFilename"]
		controller.updateCandidate(candidateID, candidateName, candidateDescription, filename)
		
		return self.displayPage(projectID, questionID, candidateID)

	def displayError(self, projectID, error):
		flash(error)
		return redirect("../../../{}/view_questions".format(projectID))
	

