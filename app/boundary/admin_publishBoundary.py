from flask import render_template, redirect, session, flash
from ..controllers.admin_publishController import admin_publishController


class publishBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projectID):
		controller = admin_publishController()
		projectDetails = controller.getProjectDetails(projectID)
		preElectionMessage = controller.getPreElectionMessage(projectID)
		invitationMessage = controller.getInvitationMessage(projectID)
		errorMessages = controller.getErrorMessages(projectID)
		print(errorMessages)

		return render_template('admin_publish.html', projectID=projectID,
													 projectDetails=projectDetails,
													 preElectionMessage=preElectionMessage,
													 invitationMessage=invitationMessage,
													 errorMessages=errorMessages,
													 userType = session['userType'])
	
	def requestVerification(self, projectID):
		controller = admin_publishController()
		result = controller.requestVerification(projectID)
		