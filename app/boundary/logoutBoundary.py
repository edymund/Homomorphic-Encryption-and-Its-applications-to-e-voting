from flask import redirect, session, flash

class logoutBoundary:
	# Empty Constructor
	def __init__(self):
		pass

	def logout(self):
		"""
		Updates the session of the current user to logged off
		"""
		session.clear()

	def redirectToLogin(self):

		flash('Logged out successfully')
		return redirect('/login')