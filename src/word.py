#
# word.py
#

import noun

import form
import sexp

COMM = 0
NOUN = 1
VERB = 2
ADJT = 3
ADVB = 4
PREP = 5
PART = 6
PTCP = 7
TRAN = 8
NUMR = 9

TYPE_LABELS = {
	COMM: "none-type",
	NOUN: "noun",
	VERB: "verb",
	ADJT: "adjective",
	ADVB: "adverb",
	PREP: "preposition",
	PART: "particle",
	PTCP: "participle",
	TRAN: "transgressive",
	NUMR: "numeral",
}

words = []

class Word:
	def __init__(self, type):
		self.type = type
		self.lemma = ""
		self.freq = 0
		self.specs = {}
		self.forms = {}
		self.errs = {}
		self.notions = []

	def print(self):
		print(TYPE_LABELS[self.type] + ": " + self.lemma)

		for k in self.specs:
			print('\t', k, "=", self.specs[k])

		for k in self.forms:
			print('\t', end='')
			form.display(k, e=' ')
			print(self.forms[k])

def init():
	err = load_words("../data/ru/nouns", noun.load, NOUN)
	if err:
		return err

	for w in words:
		w.print()

def load_words(path, func, type):
	sx, err = sexp.load_file(path)
	if err:
		return err

	for sub in sx:
		if len(sub) < 3:
			return "Too few word args: " + str(sub)

		if isinstance(sub[0], list):
			return "Wrong lemma: " + str(sub)

		if len(sub[0]) == 0:
			return "Empty lemma: " + str(sub)

		w = Word(type)
		w.lemma = sub[0]
		w.freq = sub[1]

		for m in sub:
			if not isinstance(m, list) or len(m) == 0:
				continue

			if m[0] == sexp.FLAGS:
				for f in m[1:]:
					w.specs[f] = True

			elif m[0] == sexp.DEF:
				if len(m) != 3:
					return "Wrong def syntax: " + str(sub)

				w.specs[m[1]] = m[2]

		w.notions = sub[2]

		err = func(w)
		if err:
			return err

		if "ex" in w.specs:
			pass

		words.append(w)
