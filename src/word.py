#
# word.py
#

import adjective
import noun
import verb

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
forms = {}

class Word:
	def __init__(self, type):
		self.type = type
		self.lemma = ""
		self.freq = 0
		self.specs = {}
		self.forms = {}
		self.errs = {}
		self.notions = []

	def string(self):
		s = ''
		s += TYPE_LABELS[self.type] + ": " + self.lemma + '\n'

		for k in self.specs:
			spec = self.specs[k]
			if isinstance(spec, bool):
				spec = str(spec)
			s += '\t' + k + ": " + spec + '\n'

		for k in self.forms:
			s += '\t'
			s += form.string(k, e=' ')
			s += self.forms[k] + '\n'

		return s

	def display(self):
		print(self.string())

def init():
	err = load_words("../data/ru/nouns", noun.load, NOUN)
	if err:
		return err

	err = load_words("../data/ru/adjectives", adjective.load, ADJT)
	if err:
		return err

	err = load_words("../data/ru/adverbs", load_dummy, ADVB)
	if err:
		return err

	err = load_words("../data/ru/particles", load_dummy, PART)
	if err:
		return err

	err = load_words("../data/ru/prepositions", load_dummy, PREP)
	if err:
		return err

	err = load_words("../data/ru/verbs", verb.load, VERB)
	if err:
		return err

	for w in words:
		for k in w.forms:
			f = w.forms[k]
			if f not in forms:
				forms[f] = set()

			forms[f].add(w)

def load_dummy(w):
	pass

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

		err = apply_forms(w, "ex", w.forms, "Wrong exception syntax")
		if err:
			return err

		err = apply_forms(w, "er", w.errs, "Wrong error-case syntax")
		if err:
			return err

		words.append(w)

def apply_forms(w, name, dt, msg):
	if name in w.specs:
		spec = w.specs[name]
		if len(spec) % 2:
			return msg + ": " + str(spec)

		for i in range(0, len(spec), 2):
			f = form.read(spec[i])
			if f is None:
				return "Wrong form: " + spec[i] + " in " + str(spec)

			dt[f] = spec[i + 1]

		del w.specs[name]

def find(s):
	for w in words:
		if s == w.lemma:
			return w
