#
# tok.py
#

import letter as lt
import word

class Tok:
	def __init__(self, s):
		self.data = s
		self.words = {}

		# TODO: ё
		low = s.lower()
		if low in word.forms:
			self.words = word.forms[low]

	def string(self):
		s = ''
		s += self.data
		if self.words:
			s += " -> "
			for w in self.words:
				s += w.lemma + ' '

		s += '\n'
		return s

	def display(self):
		print(self.string())

def tokenize(s):
	line = s.split()
	chain = []
	for bit in line:
		if len(bit):
			while lt.is_punc(bit[0]):
				chain.append(Tok(bit[0]))
				bit = bit[1:]
				if len(bit) == 0:
					break

		tail = []
		if len(bit):
			while lt.is_punc(bit[-1]):
				tail.append(Tok(bit[-1]))
				bit = bit[:-1]
				if len(bit) == 0:
					break

		chain.append(Tok(bit))

		if tail:
			chain += tail

	return chain
