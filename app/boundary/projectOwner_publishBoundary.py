from flask import render_template, redirect, session, flash
from ..controllers.projectOwner_publishController import projectOwner_publishController


class publishBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projectID):
		controller = projectOwner_publishController()
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
	
	def displayError(self, projectID, error):
		flash(error)
		return self.displayPage(projectID)

	def requestVerification(self, projectID):
		controller = projectOwner_publishController()
		if controller.requestVerification(projectID):
			self.send_mail(projectID)
			return redirect('/mainballot')
		else:
			return self.displayError(projectID)

	def verifyProject(self, projectID):
		controller = projectOwner_publishController()
		# Set user's approval to True
		if controller.verifyProject(projectID, session['organizerID']):
			# Check if all user has approved, if yes change status of project
			controller.updateProjectStatusToPublished(projectID)
			controller.generate_inv_msg(projectID)
		return self.displayPage(projectID)
	
	def send_mail(self,projectID):
		controller = projectOwner_publishController()
		verifier_arr = controller.get_all_verifier(projectID)
		if len(verifier_arr) >0:
			controller.notify_verifier(verifier_arr)
		else:
			controller.generate_inv_msg(projectID)
	
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
	
	
