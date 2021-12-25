from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.voters_ViewVoterCoverPage import voters_ViewVoterCoverPage
from .boundary.voters_ViewVotingPage import voters_ViewVotingPage
from .boundary.voters_ViewSubmittedVotePage import voters_ViewSubmittedVotePage
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

@app.route('/ViewVoterCoverPage', methods=['GET'])
def viewVoterCoverPage():
	# Create a boundary object
	boundary = voters_ViewVoterCoverPage()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/ViewVotingPage', methods=['GET'])
def viewVotingPage():
	# Create a boundary object
	boundary = voters_ViewVotingPage()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/ViewSubmittedVotePage', methods=['GET'])
def viewSubmittedVotePage():
	# Create a boundary object
	boundary = voters_ViewSubmittedVotePage()
	if request.method == 'GET':
		return boundary.displayPage()
