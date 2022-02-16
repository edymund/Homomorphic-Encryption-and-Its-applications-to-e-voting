import smtplib
from email.message import EmailMessage

class SendEmailService:
	def __init__(self, senderEmail=None, senderPassword=None, serverAddress=None, portNumber=None, recepientEmail=[]):
		self.setLoginDetails(senderEmail, senderPassword)
		self.setServer(serverAddress, portNumber)
		self.setRecepientEmail(recepientEmail)

	def setLoginDetails(self, senderEmail, senderPassword):
		self.senderEmail = senderEmail
		self.senderPassword = senderPassword
	
	def setServer(self, serverAddress, portNumber):
		self.server = serverAddress
		self.port = portNumber
	
	def setMessage(self, subject, message):
		self.subject = subject
		self.message = message

	def setRecepientEmail(self, recepientEmail):
		'''
		Takes in a single email or a list of email address
		'''
		if type(recepientEmail) is not list:
			self.recepientEmails = [recepientEmail]
		else:
			self.recepientEmails = recepientEmail

	def sendEmail(self):
		'''
		Sends email once all the parameters are included
		'''
		# Verify all parameters are set
		if not self.__verifyFieldsSet__():
			return False
			

		# Sends Email
		with smtplib.SMTP(self.server, self.port) as smtp:
			smtp.ehlo()			# Identify yourself to server
			smtp.starttls()		# Start TLS connection
			smtp.ehlo()			# Identify yourself using TLS

			# Logs into the server
			smtp.login(self.senderEmail, self.senderPassword) 
			
			# Sends Email to all recepients
			for recepient in self.recepientEmails:
				email = self.__setMail__(recepient)
				smtp.send_message(email)
			
			# Logout of server
			smtp.quit()
		return True

	def __setMail__(self, recepient):

		email = EmailMessage()
		email['From'] = self.senderEmail
		email['To'] = recepient
		email["Subject"] = self.subject
		email.set_content(self.message)

		return email
	
	def __verifyFieldsSet__(self):
		if self.senderEmail is None or \
			self.senderPassword is None or \
			self.server is None or \
			self.port is None or \
			self.subject is None or \
			self.message is None:
			return False
		return True


			