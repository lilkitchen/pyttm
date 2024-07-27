#
# token.py
#

import letter as lt
import word

class Token:
	def __init__(self, s):
		self.data = s
		self.words = {}

		if s in word.forms:
			self.words = word.forms[s]

	def display(self):
		print(self.data, end='')
		if self.words:
			print(" -> ", end='')
			for w in self.words:
				print(w.lemma, end=' ')

		print("")

def tokenize(s):
	line = s.split()
	chain = []
	for bit in line:
		if len(bit):
			while lt.is_punc(bit[0]):
				chain.append(Token(bit[0]))
				bit = bit[1:]
				if len(bit) == 0:
					break

		tail = []
		if len(bit):
			while lt.is_punc(bit[-1]):
				tail.append(Token(bit[-1]))
				bit = bit[:-1]
				if len(bit) == 0:
					break

		chain.append(Token(bit))

		if tail:
			chain += tail

	return chain
