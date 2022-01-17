from flask import render_template, redirect, session, flash
import pandas as pd
from ..controllers.organizer_ImportVoterListController import organizer_importVoterListController

class organizer_importVoterListBoundary:
	# Constructor
	def __init__(self,projectID= None):
		self.projectID = projectID
	
	def getProjID(self):
		return self.projectID

	# mutator
	def setProjID(self,projID):
		self.projectID = projID

	# Other Methods
	def displayPage(self):
		vList = self.getVoterList()
		status = self.check_validity(vList)
		return render_template('organizer_ImportVotersList.html', voterList =vList, 
															 projectID = self.projectID,
															 userType=session['userType'],
															 status= status
															 )
	
	def onSubmit(self, fileName):
		controller = organizer_importVoterListController(projID = self.getProjID())
		col_names=["Email"]
		try:
			datas = pd.read_csv(fileName, names = col_names)
		except UnicodeDecodeError:
			flash("Please upload a CSV file","error")
			return 1
		vList = datas.Email.to_list()
		status = self.check_validity(vList)
		if status:
			controller.update_voter(self.projectID,vList)
			flash("Uploaded successfully")
		return status

	def getVoterList(self):
		controller = organizer_importVoterListController(projID = self.getProjID())
		voters_list = controller.get_all_voters_email()
		return voters_list
	
	def check_validity(self,vList):
		"""
		return 0 if all good
		return 1 if not in csv
		return 2 if email wrong format
		return 3 if csv not in correct format
		"""
		for email in vList:
			if email.find("@") < 0:
				flash("Invalid email in CSV, please rectify and re-upload","error")
				return False
		return True

	