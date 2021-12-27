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
		return self.projectID

	# mutator
	def setProjID(self,projID):
		self.projectID = projID
	
	def setPreMsg(self,preMsg):
		self.preMsg = preMsg
	
	def setPostMsg(self,postMsg):
		self.postMsg = postMsg

	# Other Methods
	def displayPage(self):

		return render_template('user_viewElectionMessage.html',preMsg = json.dumps(self.preMsg), postMsg =json.dumps(self.postMsg))
	
	def onSubmit(self, preMsg, postMsg):
		controller = ElectionMsgController(projID = self.getProjID())
		if controller.check_pre_election_msg(preMsg):
			pass
		if controller.check_post_election_msg(postMsg):
			pass
		# proceed to update table

	def get_post_msg(self):
		pass

	def get_pre_msg(self):
		pass