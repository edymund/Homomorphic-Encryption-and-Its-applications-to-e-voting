import os.path
import json

from flask import render_template, redirect, session, flash, send_file, current_app
from ..controllers.organizer_downloadResultsController import organizer_downloadResultsController

class organizer_downloadResultsBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self, projectID):
		controller = organizer_downloadResultsController()
		projectStatus = controller.getProjectStatus(projectID)
		totalNumberOfVoters = controller.getTotalNumberOfVoters(projectID)
		numberOfVotersVoted = controller.getNumberOfVotersVoted(projectID)

		return render_template('organizer_downloadResults.html', projectID=projectID,
																 userType=session['userType'],
																 projectStatus=projectStatus,
																 totalVotes=totalNumberOfVoters,
																 uniqueVotes=numberOfVotersVoted)
	
	def downloadFile(self, projectID):
		downloadFolder = current_app.config["DOWNLOAD_FOLDER"]
		path = os.path.join(current_app.root_path, downloadFolder, 'votingResult', f'result_{projectID}.encrypt')
		
		# If the path does not exist, create a file and write data
		controller = organizer_downloadResultsController()
		AES_key = current_app.config.get("AES_KEY")
		data = controller.getEncryptedVotingData(projectID, AES_key)
		with open(path, "w") as f:
			f.write(data)
		
		return send_file(path, as_attachment=True)