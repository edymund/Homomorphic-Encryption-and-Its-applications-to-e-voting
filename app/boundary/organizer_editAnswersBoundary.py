from ..controllers.organizer_editAnswersController import organizer_editAnswersController
from flask import render_template, flash, redirect, session

class organizer_editAnswersBoundary:
	def __init__(self):
		self.ERROR_UNAUTHROIZED = "Not authorized to access the requested resource"

	def hasPermission(self, projectID, questionID, candidateID):
		controller = organizer_editAnswersController()
		return controller.checkPermission(projectID, questionID, candidateID)

	def displayPage(self, projectID, questionID, candidateID):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError(projectID,questionID, self.ERROR_UNAUTHROIZED)

		controller = organizer_editAnswersController()
		projectName = controller.getProjectName(projectID)
		projectStatus = controller.getProjectStatus(projectID)
		candidateDetails = controller.getCandidateDetails(candidateID)

		return render_template('organizer_editAnswers.html', projectID=projectID,
															 projectStatus=projectStatus,
														 	 projectName=projectName, 
														 	 candidate=candidateDetails,
														 	 userType=session['userType'])
	
	def updateCandidate(self, projectID, questionID, candidateID, candidateName, candidateDescription, filename):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError(projectID,questionID, self.ERROR_UNAUTHROIZED)
		
		controller = organizer_editAnswersController()
		# existingFilename = controller.getCandidateDetails(candidateID)["imageFilename"]
		controller.updateCandidate(candidateID, candidateName, candidateDescription, filename)
		
		return self.displayPage(projectID, questionID, candidateID)

	def displayError(self, projectID,questionID, error):
		flash(error,'error')
		return redirect("../../../{}/edit_questions/{}".format(projectID, questionID))
	
	def displaySuccess(self, projectID, questionID):
		return redirect("../../../{}/edit_questions/{}".format(projectID, questionID))
	
	def deleteCandidate(self, projectID, questionID, candidateID):
		if not self.hasPermission(projectID, questionID, candidateID):
			return self.displayError(projectID,questionID, self.ERROR_UNAUTHROIZED)

		controller = organizer_editAnswersController()
		if controller.deleteCandidate(projectID, questionID, candidateID):
			return self.displaySuccess(projectID, questionID)
		else:
			return self.displayError(projectID,questionID, "Failed to delete candidate")
	
	def addNewCandidate(self, projectID, questionID, candidateName, candidateDescription, filename):
		controller = organizer_editAnswersController()
		return controller.addNewCandidate(projectID, questionID, candidateName, candidateDescription, filename)

	def getProjectStatus(self,projectID):
		controller = organizer_editAnswersController()
		return controller.getProjectStatus(projectID)
