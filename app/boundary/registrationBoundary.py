from sqlite3.dbapi2 import IntegrityError
from flask import render_template, session, redirect, request, flash
from ..controllers.registrationController import registrationController

class registrationBoundary:
	# Constructor
	def __init__(self):
		self.RESULT_FAILURE_DUPLICATE_VALUE = "{}: {} already exists"
		self.RESULT_SUCCESS = "Success"
		self.PASSWORD_INVALID = "Passwords does not match"

	# Other Methods
	def displayPage(self):
		return render_template('registration.html')

	
	def onSubmit(self,email,password,cfm_password,companyName,firstName,lastName):
		controller = registrationController()
		if password != cfm_password:
			return self.PASSWORD_INVALID
		else:
			try:
				controller.addUser(email,password,companyName,firstName,lastName)
				return self.RESULT_SUCCESS
			except IntegrityError:
				return self.RESULT_FAILURE_DUPLICATE_VALUE.format('Email', email)

	
	def displaySuccess(self):
		flash("Account created successfully", 'message')
		return redirect('/login')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/registration')