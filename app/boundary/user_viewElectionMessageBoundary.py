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
	def displayPage(self):
		preMsg = self.get_pre_msg()
		postMsg = self.get_post_msg()
		return render_template('user_viewElectionMessage.html',preMsg = json.dumps(self.preMsg), postMsg =json.dumps(self.postMsg))
	
	def onSubmit(self, preMsg, postMsg):
		controller = ElectionMsgController(projID = self.getProjID())
		if controller.check_pre_election_msg(preMsg):
			controller.update_pre_election_msg(preMsg)
		if controller.check_post_election_msg(postMsg):
			controller.update_post_election_msg(postMsg)
		# proceed to update table

	def get_post_msg(self):
		controller = ElectionMsgController(projID = self.getProjID())
		return controller.retrieve_post_election_msg()

	def get_pre_msg(self):
		controller = ElectionMsgController(projID = self.getProjID())
		return controller.retrieve_pre_election_msg()