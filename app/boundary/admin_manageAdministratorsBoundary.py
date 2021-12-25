from flask import render_template
class admin_manageAdministratorsBoundary:
	def __init__(self):
		pass

	def displayPage(self, projectID):
		return render_template('admin_manageAdministrators.html', projectID=projectID)
	
	def addAdministrator(self, projectID):
		return self.displayPage(projectID)