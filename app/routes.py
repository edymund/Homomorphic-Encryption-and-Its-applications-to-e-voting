from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from app import application as app, boundary, loginRequired
from flask import request

@app.route('/', methods=['GET'])
def landingPage():
	# Creates a boundary object
	boundary = landingPageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/edit_profile', methods=['GET'])
def editProfilePage():
	# Create a boundary object
	boundary = user_editProfileBoundary()
	if request.method == 'GET':
		return boundary.displayPage()