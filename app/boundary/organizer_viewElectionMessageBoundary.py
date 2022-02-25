from flask import render_template, flash, redirect, session
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
		return render_template('organizer_viewElectionMessage.html', preMsg = preMsg, 
																	 postMsg= postMsg, 
																	 projectID=projectID,
																	 projectStatus=projectStatus,
																	 userType=session['userType'])

	def onSubmit(self, preMsg, postMsg,projectID):
		controller = ElectionMsgController(projectID)
		controller.update_pre_election_msg(preMsg,projectID)
		controller.update_post_election_msg(postMsg,projectID)


	
	def getProjectStatus(self,projectID):
		controller = ElectionMsgController(projectID)
		return controller.getProjectStatus(projectID)
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)
