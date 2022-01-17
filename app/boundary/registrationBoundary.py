from sqlite3.dbapi2 import IntegrityError
from flask import render_template, session, redirect, request, flash
from ..controllers.registrationController import registrationController
import re

class registrationBoundary:
	# Constructor
	def __init__(self):
		self.RESULT_FAILURE_DUPLICATE_VALUE = "{}: {} already exists"
		self.RESULT_SUCCESS = "Success"

	# Other Methods
	def displayPage(self):
		return render_template('registration.html')

	def __checkIsValidPassword(self, password, cfm_password):
		# Check if passwords match
		if password != cfm_password:
			self.ERROR = "Password fields do not match"
			return False
		return True

	def __checkIsValidFullName(self, firstName, lastName):
		# Check first name, last name
		if not re.search('^[a-zA-Z]+$', firstName) or \
			not re.search('^[a-zA-Z]+$', lastName):
			self.ERROR = "Name contain invalid characters"
			return False
		return True

	def __checkEmailFormat(self,email):
		# Check first name, last name
		if not re.search('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', email):
				self.ERROR = "Email format is not valid"
				return False
		return True

	def __checkPasswordRequirements(self, password):
		# Check if passwords match 
		if not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$', password):
			self.ERROR = "Password needs to contain at least 1 lowercase, 1 uppercase and 1 digit"
			return False
		if not re.search('.{8}$', password):
			self.ERROR = "Password must have minimum length of 8 characters"
			return False
		return True

	def onSubmit(self,email,password,cfm_password,companyName,firstName,lastName):
		if self.__checkIsValidFullName(firstName, lastName) and \
			self.__checkIsValidPassword(password, cfm_password) and \
			self.__checkEmailFormat(email) and \
			self.__checkPasswordRequirements(password):
			try:
				controller = registrationController
				controller.addUser(self,email,password,companyName,firstName,lastName)
				return self.RESULT_SUCCESS
			except IntegrityError:
				return self.RESULT_FAILURE_DUPLICATE_VALUE.format('Email', email)
		else:
			return self.ERROR
	
	
	def displaySuccess(self):
		flash("Account created successfully", 'message')
		return redirect('/login')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/registration')