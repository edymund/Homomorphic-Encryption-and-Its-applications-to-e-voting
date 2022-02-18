from ..controllers.projectOwner_editAnswersController import projectOwner_editAnswersController
from flask import render_template, flash, redirect, session

class projectOwner_editAnswersBoundary:
	def __init__(self):
		self.ERROR_UNAUTHROIZED = "Not authorized to access the requested resource"

	def hasPermission(self, projectID, questionID, candidateID):
		controller = projectOwner_editAnswersController()
		return controller.checkPermission(projectID, questionID, candidateID)

	def displayPage(self, projectID, questionID, candidateID):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError(projectID, self.ERROR_UNAUTHROIZED)

		controller = projectOwner_editAnswersController()
		projectName = controller.getProjectName(projectID)
		candidateDetails = controller.getCandidateDetails(candidateID)

		return render_template('organizer_editAnswers.html', projectID=projectID, 
														 projectName=projectName, 
														 candidate=candidateDetails,
														 userType=session['userType'])
	
	def updateCandidate(self, projectID, questionID, candidateID, candidateName, candidateDescription, filename):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError(projectID, self.ERROR_UNAUTHROIZED)
		
		controller = projectOwner_editAnswersController()
		# existingFilename = controller.getCandidateDetails(candidateID)["imageFilename"]
		controller.updateCandidate(candidateID, candidateName, candidateDescription, filename)
		
		return self.displayPage(projectID, questionID, candidateID)

	def displayError(self, projectID, error):
		flash(error)
		return redirect("../../../{}/view_questions".format(projectID))
	
	def displaySuccess(self, projectID, questionID):
		return redirect("../../../{}/edit_questions/{}".format(projectID, questionID))
	
	def deleteCandidate(self, projectID, questionID, candidateID):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError(projectID, self.ERROR_UNAUTHROIZED)

		controller = projectOwner_editAnswersController()
		if controller.deleteCandidate(projectID, questionID, candidateID):
			return self.displaySuccess(projectID, questionID)
		else:
			return self.displayError(projectID, "Failed to delete candidate")

	def getNewCandidateID(self):
		controller = projectOwner_editAnswersController()
		return controller.getNewCandidateID()
	
	def addNewCandidate(self, projectID, questionID, candidateName, candidateDescription, filename):
		controller = projectOwner_editAnswersController()
		return controller.addNewCandidate(projectID, questionID, candidateName, candidateDescription, filename)
