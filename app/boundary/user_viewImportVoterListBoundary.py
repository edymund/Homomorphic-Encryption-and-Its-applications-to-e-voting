from flask import render_template, redirect, session
from ..controllers.ImportVoterListController import ImportVoterListController
import json

class user_viewImportVoterListBoundary:
	# Constructor
	def __init__(self,projectID= None):
		self.projectID = projectID
	
	def getProjID(self):
		return self.projectID

	# mutator
	def setProjID(self,projID):
		self.projectID = projID

	# Other Methods
	def displayPage(self,vList=None):
		return render_template('user_importVotersList.html', voterList =json.dumps(vList), 
															 projectID = self.projectID,
															 userType=session['userType'])
	
	def onSubmit(self, fileName):
		# pass
		controller = ImportVoterListController(projID = self.getProjID())
		if controller.processVoterList(fileName):
			controller.update_voter(self.projectID)
		

	def populateTextArea(self):
		controller = ImportVoterListController(projID = self.getProjID())
		# controller.setProjID()
		voters_list = controller.get_all_voters_email()
		return voters_list