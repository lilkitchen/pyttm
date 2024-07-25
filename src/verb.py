#
# verb.py
#

import form as fm

def load(w):
	if len(w.lemma) < 3:
		return

	end = w.lemma[-3:]

	f = 0
	final = ['', '', '', '']
	lemma = w.lemma
	if end[-2:] == 'ся' or end[-2:] == 'сь':
		f |= fm.RFX
		final[0] = 'ся'
		final[1] = 'сь'
		if "pf" in w.specs:
			final[2] = 'ся'
		else:
			final[2] = 'сь'
		final[3] = 'вшись'
		lemma = lemma[:-2]
		end = lemma[-3:]

	if "conj" not in w.specs:
		if end[0] == 'и':
			w.specs["conj"] = "2"

		else:
			w.specs["conj"] = "1"

	conj = w.specs["conj"]

	print(w.lemma, lemma)
	w.forms[f | fm.INF] = w.lemma

	if "pf" in w.specs:
		incline_past(w, f, lemma, final)

	elif "no-pres" not in w.specs:
		if conj == "1":
			w.forms[f | fm.SG | fm.PRES | fm.FST] = lemma[:-2] + "ю" + final[2]
			w.forms[f | fm.SG | fm.PRES | fm.SEC] = lemma[:-2] + "ешь" + final[0]
			w.forms[f | fm.SG | fm.PRES | fm.TRD] = lemma[:-2] + "ет" + final[0]
			w.forms[f | fm.PL | fm.PRES | fm.TRD] = lemma[:-2] + "ют" + final[0]

		elif conj == "2":
			w.forms[f | fm.SG | fm.PRES | fm.FST] = lemma[:-3] + "ю" + final[0]
			w.forms[f | fm.SG | fm.PRES | fm.SEC] = lemma[:-3] + "ишь" + final[0]
			w.forms[f | fm.SG | fm.PRES | fm.TRD] = lemma[:-3] + "ит" + final[0]
			w.forms[f | fm.PL | fm.PRES | fm.TRD] = lemma[:-3] + "ят" + final[0]

		incline_past(w, f, lemma, final)

	# TODO: imperative, etc.

	if "pres" in w.specs:
		spec = w.specs["pres"]
		if len(spec) != 4:
			return "Wrong pres form count: " + spec

		w.forms[f | fm.SG | fm.PRES | fm.FST] = spec[0]
		w.forms[f | fm.SG | fm.PRES | fm.SEC] = spec[1]
		w.forms[f | fm.SG | fm.PRES | fm.TRD] = spec[2]
		w.forms[f | fm.PL | fm.PRES | fm.TRD] = spec[3]
		del w.specs["pres"]

	if "past" in w.specs:
		spec = w.specs["past"]
		if len(spec) != 3:
			return "Wrong pres past count: " + spec

		w.forms[f | fm.SG | fm.PAST | fm.MAS] = spec[0]
		w.forms[f | fm.SG | fm.PAST | fm.FEM] = spec[1]
		w.forms[f | fm.SG | fm.PAST | fm.COM] = spec[1][:-1] + 'о'
		w.forms[f | fm.PL | fm.PAST | fm.TRD] = spec[2]
		del w.specs["past"]

	if "futr" in w.specs:
		spec = w.specs["futr"]
		if len(spec) != 4:
			return "Wrong pres futr count: " + spec

		w.forms[f | fm.SG | fm.FUTR | fm.FST] = spec[0]
		w.forms[f | fm.SG | fm.FUTR | fm.SEC] = spec[1]
		w.forms[f | fm.SG | fm.FUTR | fm.TRD] = spec[2]
		w.forms[f | fm.PL | fm.FUTR | fm.TRD] = spec[3]
		del w.specs["futr"]

def incline_past(w, f, lemma, final):
	w.forms[f | fm.SG | fm.PAST | fm.MAS] = lemma[:-2] + "л" + final[0]
	w.forms[f | fm.SG | fm.PAST | fm.FEM] = lemma[:-2] + "ла" + final[1]
	w.forms[f | fm.SG | fm.PAST | fm.COM] = lemma[:-2] + "ло" + final[1]
	w.forms[f | fm.PL | fm.PAST | fm.TRD] = lemma[:-2] + "ли" + final[1]


# number
# gender
# tense
# person
# aspect
# voice
