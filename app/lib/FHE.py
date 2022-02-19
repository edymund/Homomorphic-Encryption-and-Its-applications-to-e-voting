# Default Parameters required 
	# public key (pk)
	# secret key (p)
	# noise (r)
	# plaintext bit (m)
	# ciphertext (c)
	# security parameter (λ - lambda)


# Parameters with Constraints in (3 - A Somewhat Hormomorphic Encryption Scheme)
	# bit-length of integers in the public key (γ - gamma)
	# bit-length of the secret key (η - eta)
	# bit-length of the noise (ρ - rho)
	# number of integers in the public key (τ - tau)
	

# Constraints
	## Definition - See: https://crypto.stackexchange.com/questions/27793/key-size-for-symmetric-homomorphic-encryption-over-the-integers
		## p = ω(logλ)  means a function that is "greater" than logλ, for instance, λ or λ^2;
		## O~(λ^5) means a function that is "smaller than or equal to" λ5⋅logkλ, for any non-negative integer k. For instance, λ^5, or λ^4;
		## Θ(λlog2λ)  means a function that "behave" like λlog2λ, for instance, any multiple like 2⋅λlog2λ, or 3⋅λlog2λ, ..., or even λlog2λ itself.

	# ρ = ω(log λ) - prevent brute force on noise
	# η ≥ ρ · Θ(λ log2 λ) - support homomorphism for deep enough circuits to evaluate "squashed decryption circuit"
	# γ = ω(η2 log λ) - prevent lattice attacks based on appromixate-gcd problem
	# τ ≥ γ + ω(log λ) - use leftover hash lemma in the reduction to approximate gcd
	# p' = ρ+ω(log λ) - secondary noise parameter

from optparse import Values
from random import randint, getrandbits, shuffle
import math
from socket import has_dualstack_ipv6
import json

class FHE:
	securityParameter = 5
	noiseBitLength = securityParameter
	secondaryNoiseBitLength = 2 * securityParameter
	secretKeyBitLength = securityParameter**2
	publicKeyBitLength = securityParameter**5
	numberOfIntegersInPublicKey = publicKeyBitLength + securityParameter
	totalNoise = 0

	# securityParameter = 5
	# noiseBitLength = securityParameter
	# secondaryNoiseBitLength = securityParameter
	# secretKeyBitLength = securityParameter**2
	# publicKeyBitLength = int(secretKeyBitLength**1.5)
	# numberOfIntegersInPublicKey = publicKeyBitLength + securityParameter

	# def __init__(cls, securityParameter):
	# 	securityParameter = securityParameter
	# 	noiseBitLength = securityParameter
	# 	secondaryNoiseBitLength = 2 * cls.securityParameter
	# 	secretKeyBitLength = cls.securityParameter**2
	# 	publicKeyBitLength = cls.securityParameter**5
	# 	numberOfIntegersInPublicKey = cls.publicKeyBitLength + cls.securityParameter

	def keyGen(self):
		'''
		1. GENERATE SECRET KEY
		2. GENERATE PUBLIC KEY BY SAMPLING X
		'''
		# print("\n\n===========Generating Keys===========")
		# GENERATE SECRET KEY
		# Determine secret key (odd integer)
		a = 2 ** (FHE.secretKeyBitLength-1) + 1
		b = 2 ** FHE.secretKeyBitLength
		p = 0
		while(p % 2 != 1):
			p = randint(a, b)
		# print("\nThe value of p(secret key) is", p)
		# print("bitlength", p.bit_length() == FHE.secretKeyBitLength)
		# print(p.bit_length())
		# print(FHE.secretKeyBitLength)

		q_upper = (2**FHE.publicKeyBitLength)//p
		r_value = 2**FHE.noiseBitLength

		def sample(p, q_upper, r_value):
			q = randint(1, q_upper)
			r = randint(-r_value, r_value)
			return int(p*q + r)

		# Sample τ numebr of values
		values = [None] * FHE.numberOfIntegersInPublicKey
		for i in range(len(values)):
			values[i] = sample(p, q_upper, r_value)

		# 1. Ensure that highest value in the list is odd
		# 2. Ensure that highest value in the list when highest value minus round(highest value/p) * p is even
		pos = values.index(max(values))
		while (values[pos] % 2 != 1) or ((values[pos] % p) % 2 != 0):
			values[pos] = sample(p, q_upper, r_value)
			pos = values.index(max(values))

		# Swap highest value with 1st value
		values.sort(reverse=True)
		# print(values.index(max(values)))
		# print(values)
		# print("completed")

		# Add Public and Private Key to instance variable
		self.publicKey = values
		self.privateKey = p

	def getPublicKey(self):
		return self.publicKey
	
	def getPublicKeyAsString(self):
		return json.dumps(self.publicKey)
	
	def getPrivateKey(self):
		return self.privateKey

	@staticmethod
	def encrypt(publicKey, bit):
		"""
		Use a random subset of the public key and a random R value
		"""
		publicKey = json.loads(publicKey)
		# print("\n\n===========Performing Encryption===========")
		noOfIntegerInPublicKey = len(publicKey)
		# print("len public key", len(publicKey))


		# Gets a random size of the subset of the public key and
		# Get a random r value
		s = randint(1, len(publicKey)-1)
		r = randint(-(2**FHE.secondaryNoiseBitLength), 2**FHE.secondaryNoiseBitLength)

		# Create a copy of the public key and shuffle it
		pk_copy = []
		for i in range(len(publicKey)):
			pk_copy.append(i)
		shuffle(pk_copy)
		
		
		# Gets the sum of a random subset
		sum_x = 0

		for i in range(0, s):
			sum_x += pk_copy[i]
		

		# Calculate the cipherText
		cipherText = 0
		sum = (bit + (2*r) + (2*sum_x))
		cipherText = sum % publicKey[0]
		# print("sum is {}, sum_x is {}, bit is {}, r is {}".format(sum, sum_x, bit , r))
		# print("CipherText is ", cipherText)

		return cipherText

	@staticmethod
	def decrypt(secretKey: int, c):
		# print("\n\n===========Performing Decryption===========")

		# Secret Key must be odd
		if (secretKey % 2 == 0):
			return randint(0, 1)

		plaintext = (c % secretKey) % 2
		# print("m is", plaintext)
		return plaintext
	
	@staticmethod
	def getEncryptedSum(encryptedValues, pk):
		pk = json.loads(pk)
		binaryList = []
		for value in encryptedValues:
			binaryList = addBit(binaryList, value)

		# Encrypted Each New Bit
		for i in range(len(binaryList)):
			if binaryList[i] == 1 or binaryList[i] == 0:
				binaryList[i] = FHE.encrypt(pk, binaryList[i])

		return binaryList
	
	@staticmethod
	def getDecryptedResult(encryptedBinaryList, sk: int):
		binaryString = ""
		for value in encryptedBinaryList:
			plaintext = FHE.decrypt(sk, value)
			binaryString += str(plaintext)
		# print(binaryString)
		return int(binaryString, 2)


def XOR(bit1, bit2):
	return bit1 ^ bit2

def AND(bit1, bit2):
	return bit1 & bit2

def half_adder(bit1, bit2):
	return (XOR(bit1, bit2), AND(bit1, bit2))

def full_adder(bit1, bit2, carry=0):
	sum1, carry1 = half_adder(bit1, bit2)
	sum2, carry2 = half_adder(sum1, carry)
	return (sum2, carry1 or carry2)

def addBit(binaryList, bit):
	if len(binaryList) == 0:
		binaryList.append(bit)
		return binaryList
	else:
		sum, carry = full_adder(binaryList[-1], bit)
		binaryList[-1] = sum

		binaryListPos = len(binaryList) - 2
		while (carry != 0):
			if (binaryListPos == -1):
				binaryList.insert(0, carry)
				break
			else:
				sum, carry = full_adder(binaryList[binaryListPos], carry)
				binaryList[binaryListPos] = sum
				binaryListPos -= 1
		return binaryList