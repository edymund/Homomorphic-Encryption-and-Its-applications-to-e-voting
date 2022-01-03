from flask import redirect, session, flash

class logoutBoundary:
	# Empty Constructor
	def __init__(self):
		pass

	def logout(self):
		"""
		Updates the session of the current user to logged off
		"""

		session['user'] = None
		session['userID'] = None
		session['adminProjectID'] = None
		session['subAdminProjectID'] = None
		print(session['user'])

	def redirectToLogin(self):

		flash('Logged out successfully')
		return redirect('/login')