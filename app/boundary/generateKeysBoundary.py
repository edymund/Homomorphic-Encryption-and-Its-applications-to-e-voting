from flask import render_template, redirect, session, flash
from ..controllers.generateKeysController import GenerateKeysController

class generateKeysBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		controller = GenerateKeysController()
		publicKey = controller.getPublicKey()
		secretKey = controller.getSecretKey()
		return render_template('generateKeys.html', publicKey=publicKey,
													secretKey=secretKey)