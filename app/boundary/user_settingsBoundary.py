from sqlite3.dbapi2 import IntegrityError
from flask import render_template, session, flash, redirect
from ..controllers.user_settingsController import user_settingsController
import sys

class user_settingsBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_FAIL = "Details not Changed"
		self.RESULT_FAILURE_DUPLICATE_VALUE = "{}: {} already exists"

	# Other Methods
	def displayPage(self):
		return render_template('user_settings.html')


	def onSubmit(self,first_name,last_name,email,company_name):
		username = session['user']

		controller = user_settingsController()

		# Calls the controller to update the user's details
		try:
			controller.updateUserDetails(username,first_name,last_name,email,company_name)
			return self.RESPONSE_SUCCESS
		except IntegrityError:
			return self.RESULT_FAILURE_DUPLICATE_VALUE.format('Email', email)

	def displaySuccess(self):
		flash("Changed Details Successfully", 'message')
		return redirect('/settings')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/settings')


