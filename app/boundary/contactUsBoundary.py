from flask import render_template, redirect, session, flash
import re
from ..lib.service_email import SendEmailService
from flask import url_for, current_app

class contactUsBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.email = SendEmailService()
		self.email.setLoginDetails(current_app.config['EMAIL']['USER'], current_app.config['EMAIL']['PASSWORD'])
		self.email.setServer(current_app.config['EMAIL']['SERVER'], current_app.config['EMAIL']['PORT'])
		self.errors = []

	# Other Methods
	def displayPage(self):
		return render_template('contactUs.html')

	def __checkIsValidName(self, name):
		# Check first name, last name
		if not re.search('^[a-zA-Z]+$', name):
			self.ERROR = "Name contain invalid characters"
			return False
		return True

	def __checkEmailFormat(self,sender_email):
		# Check first name, last name
		if not re.search('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', sender_email):
				self.ERROR = "Email format is not valid"
				return False
		return True

	def send_email(self,sender_email,name,subject,feedback):
		message = f"{sender_email}+ '\r\n\r\nName: ' + {name} + '\r\n\r\nFeedback: ' + {feedback}" 
		self.email.setMessage(subject, feedback)
		self.email.setRecepientEmail(current_app.config['EMAIL']['USER'])
		self.email.sendEmail()


	def onSubmit(self,sender_email,name,subject,feedback):
		if self.__checkIsValidName(name) and \
			self.__checkEmailFormat(sender_email):
			self.send_email(sender_email,name,subject,feedback)
			return self.RESPONSE_SUCCESS
		else:
			return self.ERROR
	
	#display success
	def displaySuccess(self):
		flash("Feedback Sent Successfully", 'message')
		return redirect('/contactUs')
	
	#display error and flash messages
	def displayError(self, message):
		flash(message, 'error')
		return redirect('/contactUs')