from flask import render_template, flash, redirect, session
from ..entity.Projectdetails import ProjectDetails
from ..controllers.organizer_ElectionMsgController import ElectionMsgController
import json

class organizer_viewElectionMessageBoundary:
	# Constructor
	def __init__(self,projectID=None):
		self.projectID = projectID

	# Other Methods
	def displayPage(self,projectID):
		controller = ElectionMsgController(self.projectID)
    
		projectStatus = controller.getProjectStatus(projectID)
		preMsg = controller.retrieve_pre_election_msg(projectID)
		postMsg = controller.retrieve_post_election_msg(projectID)
		self.process_pre_msg(preMsg,projectID)
		self.process_post_msg(postMsg,projectID)
		return render_template('organizer_viewElectionMessage.html', preMsg = preMsg, 
																	 postMsg= postMsg, 
																	 projectID=projectID,
																	 projectStatus=projectStatus,
																	 userType=session['userType'])

	def onSubmit(self, preMsg, postMsg,projectID):
		self.process_pre_msg(preMsg,projectID)
		self.process_post_msg(postMsg,projectID)

	def process_pre_msg(self, preMsg,projectID):
		controller = ElectionMsgController(projectID)
		if controller.check_msg(preMsg):
			controller.update_pre_election_msg(preMsg,projectID)
		elif not controller.check_msg(preMsg):
			msg = "Enjoy your voting"
			controller.update_pre_election_msg(msg,projectID)

	def process_post_msg(self, postMsg,projectID):
		controller = ElectionMsgController(projectID)
		if controller.check_msg(postMsg):
			controller.update_post_election_msg(postMsg,projectID)
		elif not controller.check_msg(postMsg):
			msg = "Hope you enjoyed your vote"
			controller.update_post_election_msg(msg,projectID)
	
	def getProjectStatus(self,projectID):
		controller = ProjectDetails(projectID)
		return controller.getStatus()
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)
