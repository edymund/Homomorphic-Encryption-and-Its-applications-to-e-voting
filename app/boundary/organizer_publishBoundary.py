from flask import render_template, redirect, session, flash, url_for
from ..controllers.projectOwner_publishController import projectOwner_publishController
from ..entity.Projectdetails import ProjectDetails

class publishBoundary:
	# Constructor
	def __init__(self):
		self.votingPageURL = url_for("voterLoginPage",_external=True)

	# Other Methods
	def displayPage(self,projectID):
		controller = projectOwner_publishController()
		projectDetails = controller.getProjectDetails(projectID)
		preElectionMessage = controller.getPreElectionMessage(projectID)
		invitationMessage = controller.getInvitationMessage(projectID)
		errorMessages = controller.getErrorMessages(projectID)
		print("Error Messages(Boundary)", errorMessages)

		return render_template('organizer_publish.html', projectID=projectID,
													 	 projectDetails=projectDetails,
														 projectStatus=projectDetails["status"],
													 	 preElectionMessage=preElectionMessage,
													 	 invitationMessage=invitationMessage,
													 	 errorMessages=errorMessages,
													 	 userType = session['userType'])
	

	# For Project Owner to Request Verification from Verifiers
	def requestVerification(self, projectID):
		controller = projectOwner_publishController()
		
		# Owner Requests for verification & update status to pending verification if possible
		# 
		if controller.requestVerification(projectID):
			# self.send_mail(projectID)
			return redirect('/mainballot')
		else:
			return self.displayError(projectID)


	# For Project Verifiers Upon Approving Project
	def verifyProject(self, projectID):
		controller = projectOwner_publishController()
		# Set user's approval to True
		if controller.verifyProject(projectID, session['organizerID']):
			# Check if all user has approved, if yes change status of project
			controller.updateProjectStatusToPublished(projectID)

		return self.displayPage(projectID)
	
	def rejectProject(self, projectID, message):
		controller = projectOwner_publishController()
		if message.strip() != "":
			controller.notify_projectOwner(projectID, message)
			controller.return_default(projectID)
			flash("Notified project owner")
			return self.displayPage(projectID)
		else:
			return self.displayError(projectID,"Please fill in feedback form")

	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)
		
	def getProjectStatus(self,projectID):
		controller = ProjectDetails(projectID)
		return controller.getStatus()
	
