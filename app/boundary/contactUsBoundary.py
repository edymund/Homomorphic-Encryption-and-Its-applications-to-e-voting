from flask import render_template, redirect, session, flash
import re
import smtplib
import json

class contactUsBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"

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
		with open("app\others\Credential.json") as f:
			email = json.load(f)
			EMAIL_ADDRESS= email["Credentials"]["Email Address"]
			EMAIL_PASSWORD = email["Credentials"]["Email Password"]
			f.close()
		server = smtplib.SMTP("smtp.gmail.com",587)
		server.starttls()
		# login(email address, password)
		server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
		msg = 'From: ' + EMAIL_ADDRESS + '\r\nTo: ' + EMAIL_ADDRESS + '\r\nSubject: Feedback: ' + subject + '\r\n\r\nFeedback received from: ' + sender_email+ '\r\n\r\nName: ' + name + '\r\n\r\nFeedback: ' + feedback 
		# sendmail(sender,receiver,message)
		server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)

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