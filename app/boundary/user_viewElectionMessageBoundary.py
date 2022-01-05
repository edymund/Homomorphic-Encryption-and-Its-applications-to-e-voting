from flask import render_template, redirect, session
from ..controllers.ElectionMsgController import ElectionMsgController
import json

class user_viewElectionMessageBoundary:
	# Constructor
	def __init__(self,projId=None):
		self.projId = projId
		self.preMsg = ""
		self.postMsg = ""

	# accessor
	def getProjID(self):
		return self.projId

	# mutator
	def setProjID(self,projID):
		self.projectID = projID
	
	def setPreMsg(self,preMsg):
		self.preMsg = preMsg
	
	def setPostMsg(self,postMsg):
		self.postMsg = postMsg

	# Other Methods
	def displayPage(self, projectID):
		controller = ElectionMsgController(projID = projectID)
		preMsg = controller.retrieve_pre_election_msg()
		postMsg = controller.retrieve_post_election_msg()
		self.process_msg(preMsg, postMsg)
		return render_template('user_viewElectionMessage.html',preMsg = json.dumps(self.preMsg), postMsg=json.dumps(self.postMsg), projectID=json.dumps(int(projectID)))

	def onSubmit(self, preMsg, postMsg):
		controller = ElectionMsgController(projID = self.projectID)
		if controller.check_election_msg(preMsg):
			controller.update_pre_election_msg(preMsg)
			self.setPreMsg(preMsg)
			
		elif not controller.check_election_msg(preMsg):
			default_pre_msg = "Enjoy your voting"
			controller.update_pre_election_msg(default_pre_msg)
			self.setPreMsg(default_pre_msg)

		if controller.check_election_msg(postMsg):
			controller.update_post_election_msg(postMsg)
			self.setPostMsg(postMsg)

		elif not controller.check_election_msg(postMsg):
			default_post_msg = "Hope you enjoyed your vote"
			controller.update_post_election_msg(default_post_msg)
			self.setPostMsg(default_post_msg)
		
	def process_msg(self, preMsg, postMsg):
		controller = ElectionMsgController(projID = self.projectID)
		if controller.check_election_msg(preMsg):
			self.setPreMsg(preMsg)
		elif not controller.check_election_msg(preMsg):
			default_pre_msg = "Enjoy your voting"
			self.setPreMsg(default_pre_msg)

		if controller.check_election_msg(postMsg):
			self.setPostMsg(postMsg)
		elif not controller.check_election_msg(postMsg):
			default_post_msg = "Hope you enjoyed your vote"
			self.setPostMsg(default_post_msg)
