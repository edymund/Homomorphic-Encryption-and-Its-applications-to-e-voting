from sqlite3.dbapi2 import IntegrityError
from flask import render_template, session, flash, redirect
from ..controllers.organizer_settingsController import organizer_settingsController
import re

class organizer_settingsBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_FAIL = "Details not Changed"
		self.RESULT_FAILURE_DUPLICATE_VALUE = "{}: {} already exists"

	# Other Methods
	def displayPage(self):
		controller = organizer_settingsController()
		username = session['user']
		data = controller.getUserDetails(username)
		return render_template('organizer_settings.html',data=data)

	def __checkIsValidFirstName(self, first_name):
		# Check first name, last name 
		if first_name != "":
			if not re.search('^[a-zA-Z]+$', first_name):
				self.ERROR = "Name contain invalid characters"
				return False
		return True

	def __checkIsValidLastName(self,last_name):
		# Check first name, last name
		if last_name != "":
			if not re.search('^[a-zA-Z]+$', last_name):
				self.ERROR = "Name contain invalid characters"
				return False
		return True

	def __checkEmailFormat(self,email):
		# Check first name, last name
		if email != "":
			if not re.search('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', email):
				self.ERROR = "Email format is not valid"
				return False
		return True

	def __checkifAllFieldsAreEmpty(self,first_name,last_name,email,company_name):
		if (first_name == "" and last_name == "" and email == "" and company_name == ""):
			self.ERROR = "Please fill in at least 1 field"
			return False
		return True

	def onSubmit(self,first_name,last_name,email,company_name):
		if self.__checkifAllFieldsAreEmpty(first_name,last_name,email,company_name) and \
			self.__checkIsValidFirstName(first_name) and \
			self.__checkIsValidLastName(last_name) and \
			self.__checkEmailFormat(email):
			try:
				username = session['user']
				controller = organizer_settingsController
				controller.updateUserDetails(self,username,first_name,last_name,email,company_name)
				return self.RESPONSE_SUCCESS
			except IntegrityError:
				return self.RESULT_FAILURE_DUPLICATE_VALUE.format('Email', email)
		else:
			return self.ERROR


	def displaySuccess(self):
		flash("Changed Details Successfully", 'message')
		return redirect('/settings')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/settings')


