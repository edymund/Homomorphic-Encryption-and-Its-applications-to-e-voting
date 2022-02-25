from ..lib.AES_CBC import AES_CBC
from ..lib.FHE import FHE

import json

class User_DecryptController:
	def __init__(self):
		pass

	def decrypt(self, encryptedData, secretKey_FHE, AES_Key):
		""" 
		Return Dictionary if Decrypt Successful
		Return None if Decrypt Failed
		"""
		AES = AES_CBC(AES_Key)
		fhe = FHE()

		try:
			votingResult = json.loads(AES.decrypt(encryptedData))
		
		
			for questionNo in range(len(votingResult["questions"])):
				for candidateNo in range(len(votingResult["questions"][questionNo]['candidate'])):
					encryptedVoteCount = votingResult["questions"][questionNo]['candidate'][candidateNo]["voteCount"]
					totalVote = fhe.getDecryptedResult(encryptedVoteCount, secretKey_FHE)
					votingResult["questions"][questionNo]['candidate'][candidateNo]["voteCount"] = totalVote
			print("Printing Decrypted Results")
			print(votingResult)

			return votingResult
		except:
			raise Exception

	def format(self, decryptedData):
		""" 
		Return String if decrypted data is correct
		Return None if decrypted data is incorrect
		"""
		try:
			message = f"""Voting Event - {decryptedData['ProjectName']}\n"""

			# Display Question
			for question in decryptedData['questions']:
				message = f"""{message}\nQuestion: {question['question']}\n"""

				for candidate in question['candidate']:
					message = f"""{message}\t{candidate['name']}: {candidate['voteCount']} votes\n"""

			return message
		except:
			raise Exception
