from flask import render_template, redirect, session, flash
from ..controllers.loginController import loginController

class loginBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_INVALID_CREDENTIALS = "Username or Password is incorrect"

	# Other Methods
	def displayPage(self):
		return render_template('login.html')
	
	def onSubmit(self, username, password):
		"""
		Firstly, verify the user's NRIC and password, then check if account 
		is suspended. Return a response based on the outcome of each check.
		"""
		# initialise a User_LoginController
		controller = loginController()

		# If credentials is incorrect
		if not controller.validateLogin(username, password):
			return self.RESPONSE_INVALID_CREDENTIALS
		
		# Otherwise, account is valid and active
		# Provide a session and return a success status
		session['user'] = username
		session['userID'] = controller.getUserID(username)

		return self.RESPONSE_SUCCESS
	
	def displaySuccess(self):
		flash("Login successfully", 'message')
		return redirect('/mainballot')
	
	def displayError(self):
		flash("Username or Password is incorrect",'error')
		return redirect('/login')

