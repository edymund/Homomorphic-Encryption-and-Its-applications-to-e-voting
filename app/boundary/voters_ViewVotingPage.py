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
		answer = ""
		questionID = ""
		candidateID = ""
		delimiter = "_"

		ansArr =[]
		count = 0
		for items in answers:
			tempArr =[]
			input = items.split(delimiter)
			answer = input[0]
			questionID = input[1]
			candidateID = input[2]
			# print(answer)
			# print(questionID)
			# print(candidateID)
			for questions in question:
					for candidate in questions["option"]:
						dictArr ={}
						# print("qid",int(candidate["questionID"]))
						# print("cid", int(candidate["candidateID"]))
						# print("if1",int(candidate["questionID"]) == int(questionID) and int(candidate["candidateID"]) == int(candidateID))
						# print("if2",int(candidate["questionID"]) == int(questionID) and int(candidate["candidateID"]) != int(candidateID))
						if int(candidate["questionID"]) == int(questionID) and int(candidate["candidateID"]) == int(candidateID):
							dictArr["candidateID"] = candidateID
							dictArr["choice"] = 1
							tempArr.append(dictArr)

						elif int(candidate["questionID"]) == int(questionID) and int(candidate["candidateID"]) != int(candidateID):
							dictArr["candidateID"] = candidate["candidateID"]
							dictArr["choice"] = 0
							tempArr.append(dictArr)
							
						else:
							ansArr.append(tempArr)
							break

						
		# print("answerArray",ansArr)
		
		if self.checkEmptyArray(ansArr):
			if controller.insertVoterAns(ansArr,6):
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
		return redirect('/'+ str(projID) + '/ViewSubmittedVotePage')

	def displayError(self, projID):
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
				


