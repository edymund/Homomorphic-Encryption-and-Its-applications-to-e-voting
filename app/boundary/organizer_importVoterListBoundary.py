from flask import render_template, redirect, session, flash
import pandas as pd
from ..controllers.organizer_ImportVoterListController import organizer_importVoterListController

class organizer_importVoterListBoundary:
	# Constructor
	def __init__(self,projectID= None):
		self.projectID = projectID

	# Other Methods
	def displayPage(self,projectID):
		controller = organizer_importVoterListController(projID = self.projectID)
		projectStatus = controller.getProjectStatus(projectID)
		vList = self.getVoterList()
		status = self.check_validity(vList)
		return render_template('organizer_ImportVotersList.html', voterList =vList, 
															 	  projectID=projectID,
															 	  projectStatus=projectStatus,
															 	  userType=session['userType'],
															 	  status= status
															 	  )
	
	def onSubmit(self, fileName):
		controller = organizer_importVoterListController(projID = self.projectID)
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
		controller = organizer_importVoterListController(projID = self.projectID)
		voters_list = controller.get_all_voters_email()
		return voters_list
	
	def check_validity(self,vList):
		"""
		return 0 if all good
		return 1 if not in csv
		return 2 if email wrong format
		return 3 if csv not in correct format
		"""
		temp_arr = []
		for email in vList:
			if email.find("@") < 0:
				self.displayError(self.projectID,"Invalid email in CSV, please rectify and re-upload")
				return False
			if email not in temp_arr:
				temp_arr.append(email)
			else:
				self.displayError(self.projectID,"Duplicated email in CSV, please rectify and re-upload")
				return False
		return True

	def getProjectStatus(self,projectID):
		controller = organizer_importVoterListController(projID = self.projectID)
		return controller.getProjectStatus(projectID)
	
	def displayError(self, projectID, errorMessage):
		flash(errorMessage,'error')
		return self.displayPage(projectID)
	