from flask import redirect, session, flash
from ..controllers.voters_loginController import voters_loginController

class voters_loginBoundary:
	# Constructor
	def __init__(self):
		pass

	def onSubmit(self, username, password, projectID):
		controller = voters_loginController()

		# If credentials is incorrect
		if controller.validateLogin(username, password, projectID):
			if controller.checkProjectStatusOngoing(projectID):
				session.clear()
				session['user'] = username
				session['userType'] = 'voter'
				session['loginType'] = 'voter'
				session['projectID'] = int(projectID)
				session['voterID'] = controller.getVoterID(username, projectID)
				print("Success")
				return self.loginSuccess(projectID)
			else:
				print("Event not available for voting")
				return self.loginFail("Event not available for voting")

		else:
			print("Invalid Credentials")
			return self.loginFail("Invalid Credentials")

		return self.loginFail()

	def loginSuccess(self, projectID):
		return redirect(f'/{projectID}/VotingMessage')

	def loginFail(self, error):
		flash(error, 'error')
		return redirect("/")