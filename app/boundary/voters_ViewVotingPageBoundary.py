from flask import render_template, redirect, session, flash
from ast import And
from flask import render_template
from app.controllers.voters_ViewVotingPageController import voters_ViewVotingPageController
import re


class voters_ViewVotingPage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projID):
		controller = voters_ViewVotingPageController()
		
		question = controller.getQuestionNCandidate(projID)

		return render_template('voters_ViewVotingPage.html',question=question,projID=projID)

	def getNumberofQuestion(self,projID):

		controller = voters_ViewVotingPageController()
		numberOfQuestion = controller.getNumberOfQuestions(projID)

		return numberOfQuestion
	
	def onSubmit(self,answers,projID):

		controller = voters_ViewVotingPageController()
		question = controller.getQuestionNCandidate(projID)

		#print(question)
		answer = None
		questionID = None
		candidateID = None
		delimiter = "_"

		ansArr =[]
		count = 0
		for items in answers:
			tempArr =[]

			# If no no vote was submitted
			input = items.split(delimiter)	# Answer_questionID_candidateID
			answer = input[0]
			questionID = input[1]
			candidateID = input[2]

			
			for questions in question:
					for candidate in questions["option"]:
						dictArr ={}
						
						# Set unselected candidate with a vote value of 0
						if (answer is None or int(candidate["candidateID"]) != int(candidateID)) and \
							int(candidate["questionID"]) == int(questionID):
							dictArr["candidateID"] = candidate["candidateID"]
							dictArr["choice"] = 0
							tempArr.append(dictArr)

						# Set selected candidate with a vote value of 1
						elif int(candidate["questionID"]) == int(questionID) and int(candidate["candidateID"]) == int(candidateID):
							dictArr["candidateID"] = candidateID
							dictArr["choice"] = 1
							tempArr.append(dictArr)
							
						else:
							ansArr.append(tempArr)
							break
		
		print("tempEmpty", tempArr)
		print("ansEmpty", ansArr)
		if self.checkEmptyArray(ansArr):
			if controller.insertVoterAns(ansArr,session['voterID'], projID):
				print("Success")
				return True
			else:
				print("Failed")
				return False
		else:
			print("Vote Voided")
			return False
		
		#display success
	def displaySuccess(self,projID):
		flash("Voting Completed")
		return redirect('/'+ str(projID) + '/ViewSubmittedVotePage')

	def displayError(self, projID):
		flash("Voting Failed")
		return redirect('/'+ str(projID) + '/ViewSubmittedVotePage')

	def checkEmptyArray(self,array):
		isNotEmpty = True
		for item in array:
			#print("array",len(item))
			if len(item) == 0:
				isNotEmpty = False
				break
			else:
				continue

		return isNotEmpty
				


