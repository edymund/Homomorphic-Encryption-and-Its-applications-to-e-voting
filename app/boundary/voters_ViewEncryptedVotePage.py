from flask import render_template

#temporary data testing
# completeinfo array will contain 1 question, 1 voter's id and 4 encryption
questions=["Q1","Q2"]
namePath = ["John Doe Me", "Eve Day You", "Haiya one Two Three", "Just ABCDESSFDJSDNDSHDJDHDSDHD"]
votersid = ["1", "2", "3", "4"]
encryptionvalues = ["dadaf532uhabd", "asj14hsad","dadaf532uhabd","dadaf532uhabd"]
votersidEncrypt = []
voterTotalinfo =[]
qanda = []
completeinfo =[]

votersidEncrypt.append(votersid[0])
votersidEncrypt.append(encryptionvalues[0])
votersidEncrypt.append(encryptionvalues[1])
votersidEncrypt.append(encryptionvalues[2])
votersidEncrypt.append(encryptionvalues[3])

voterTotalinfo.append(votersidEncrypt)
votersidEncrypt = []

votersidEncrypt.append(votersid[1])
votersidEncrypt.append(encryptionvalues[0])
votersidEncrypt.append(encryptionvalues[1])
votersidEncrypt.append(encryptionvalues[2])
votersidEncrypt.append(encryptionvalues[3])

voterTotalinfo.append(votersidEncrypt)
votersidEncrypt = []

votersidEncrypt.append(votersid[2])
votersidEncrypt.append(encryptionvalues[0])
votersidEncrypt.append(encryptionvalues[1])
votersidEncrypt.append(encryptionvalues[2])
votersidEncrypt.append(encryptionvalues[3])

voterTotalinfo.append(votersidEncrypt)
votersidEncrypt = []

votersidEncrypt.append(votersid[3])
votersidEncrypt.append(encryptionvalues[0])
votersidEncrypt.append(encryptionvalues[1])
votersidEncrypt.append(encryptionvalues[2])
votersidEncrypt.append(encryptionvalues[3])

voterTotalinfo.append(votersidEncrypt)

qanda.append(questions[0])
qanda.append(voterTotalinfo)

completeinfo.append(qanda)
qanda=[]

qanda.append(questions[1])
qanda.append(voterTotalinfo)

completeinfo.append(qanda)



class voters_ViewEncryptedVotePage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('voters_ViewEncryptedVotePage.html',completeinfo=completeinfo,candidatename=namePath)