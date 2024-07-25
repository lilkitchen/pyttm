#
# noun.py
#

import form as fm
import letter as lt

def load(w):
	end = w.lemma[-1]

	if "decl" not in w.specs:
		if end == 'ь':
			w.specs["decl"] = '3'

		elif end == 'а' or end == 'я':
			w.specs["decl"] = '1'

		else:
			w.specs["decl"] = '2'

	try:
		decl = int(w.specs["decl"])
	except ValueError:
		return "Wrong noun declension: " + w.specs["decl"] + " in " + w.lemma

	if "gender" not in w.specs:
		if decl == 1 or decl == 3:
			w.specs["gender"] = "fem"

		elif decl == 2:
			if end == 'е' or end == 'ё' or end == 'о':
				w.specs["gender"] = "com"

			else:
				w.specs["gender"] = "mas"

		else:
			return "Wrong noun declension: " + w.specs["decl"] + " in " + w.lemma

	if "no-decl" in w.specs:
		w.forms[fm.SG | fm.NOM | fm.NRM] = w.lemma
		w.forms[fm.SG | fm.GEN | fm.NRM] = w.lemma
		w.forms[fm.SG | fm.DAT | fm.NRM] = w.lemma
		w.forms[fm.SG | fm.ACC | fm.NRM] = w.lemma
		w.forms[fm.SG | fm.INS | fm.NRM] = w.lemma
		w.forms[fm.SG | fm.ADP | fm.NRM] = w.lemma
		return

	if "plural-only" not in w.specs:
		incline_singular(w, decl, w.lemma, fm.NRM)
		if "singular-only" not in w.specs:
			incline_plural(w, decl, w.lemma, fm.NRM)

	if "sg" in w.specs:
		spec = w.specs["sg"]
		if len(spec) != 5:
			return "Wrong sg form count: " + spec

		w.forms[fm.SG | fm.GEN | fm.NRM] = spec[0]
		w.forms[fm.SG | fm.DAT | fm.NRM] = spec[1]
		w.forms[fm.SG | fm.ACC | fm.NRM] = spec[2]
		w.forms[fm.SG | fm.INS | fm.NRM] = spec[3]
		w.forms[fm.SG | fm.ADP | fm.NRM] = spec[4]
		del w.specs["sg"]

	if "pl" in w.specs:
		spec = w.specs["pl"]
		if len(spec) != 6:
			return "Wrong sg form count: " + spec

		w.forms[fm.PL | fm.NOM | fm.NRM] = spec[0]
		w.forms[fm.PL | fm.GEN | fm.NRM] = spec[1]
		w.forms[fm.PL | fm.DAT | fm.NRM] = spec[2]
		w.forms[fm.PL | fm.ACC | fm.NRM] = spec[3]
		w.forms[fm.PL | fm.INS | fm.NRM] = spec[4]
		w.forms[fm.PL | fm.ADP | fm.NRM] = spec[5]
		del w.specs["pl"]

def incline_singular(w, decl, lemma, size):
	gender, end, final = incline_vars_get(w, lemma)

	w.forms[fm.SG | fm.NOM | size] = lemma

	if decl == 1:
		if end == 'а':
			w.forms[fm.SG | fm.GEN | size] = lemma[:-1] + final[0]
			w.forms[fm.SG | fm.DAT | size] = lemma[:-1] + 'е'
			w.forms[fm.SG | fm.ACC | size] = lemma[:-1] + 'у'
			w.forms[fm.SG | fm.INS | size] = lemma[:-1] + 'ой'
			w.forms[fm.SG | fm.ADP | size] = lemma[:-1] + 'е'

		elif end == 'я':
			w.forms[fm.SG | fm.GEN | size] = lemma[:-1] + 'и'
			w.forms[fm.SG | fm.DAT | size] = lemma[:-1] + final[1]
			w.forms[fm.SG | fm.ACC | size] = lemma[:-1] + 'ю'
			w.forms[fm.SG | fm.INS | size] = lemma[:-1] + 'ей'
			w.forms[fm.SG | fm.ADP | size] = lemma[:-1] + final[1]

	elif decl == 2:
		if gender == "mas":
			if end == 'ь':
				w.forms[fm.SG | fm.GEN | size] = lemma[:-1] + 'я'
				w.forms[fm.SG | fm.DAT | size] = lemma[:-1] + 'ю'
				w.forms[fm.SG | fm.ACC | size] = lemma
				w.forms[fm.SG | fm.INS | size] = lemma[:-1] + 'ем'
				w.forms[fm.SG | fm.ADP | size] = lemma[:-1] + 'е'

			else:
				w.forms[fm.SG | fm.GEN | size] = lemma + 'а'
				w.forms[fm.SG | fm.DAT | size] = lemma + 'у'
				w.forms[fm.SG | fm.ACC | size] = lemma
				w.forms[fm.SG | fm.INS | size] = lemma + final[5]
				w.forms[fm.SG | fm.ADP | size] = lemma + 'е'

		else:
			w.forms[fm.SG | fm.GEN | size] = lemma[:-1] + final[2]
			w.forms[fm.SG | fm.DAT | size] = lemma[:-1] + final[3]
			w.forms[fm.SG | fm.ACC | size] = lemma
			w.forms[fm.SG | fm.INS | size] = lemma[:-1] + final[4]
			w.forms[fm.SG | fm.ADP | size] = lemma[:-1] + final[1]

	elif decl == 3:
		w.forms[fm.SG | fm.GEN | size] = lemma[:-1] + 'и'
		w.forms[fm.SG | fm.DAT | size] = lemma[:-1] + 'и'
		w.forms[fm.SG | fm.ACC | size] = lemma
		w.forms[fm.SG | fm.INS | size] = lemma + 'ю'
		w.forms[fm.SG | fm.ADP | size] = lemma[:-1] + 'и'

	if "animated" in w.specs and w.specs["gender"] == "mas":
		w.forms[fm.SG | fm.ACC | fm.NRM] = w.forms[fm.SG | fm.GEN | fm.NRM]

def incline_plural(w, decl, lemma, size):
	gender, end, final = incline_vars_get(w, lemma)

	if decl == 1:
		if end == 'а':
			w.forms[fm.PL | fm.NOM | size] = lemma[:-1] + final[0]
			w.forms[fm.PL | fm.GEN | size] = lemma[:-1]
			w.forms[fm.PL | fm.DAT | size] = lemma[:-1] + 'ам'
			w.forms[fm.PL | fm.ACC | size] = lemma[:-1] + final[0]
			w.forms[fm.PL | fm.INS | size] = lemma[:-1] + 'ами'
			w.forms[fm.PL | fm.ADP | size] = lemma[:-1] + 'ах'

		elif end == 'я':
			w.forms[fm.PL | fm.NOM | size] = lemma[:-1] + 'и'
			w.forms[fm.PL | fm.GEN | size] = lemma[:-1] + 'й'
			w.forms[fm.PL | fm.DAT | size] = lemma + 'м'
			w.forms[fm.PL | fm.ACC | size] = lemma[:-1] + 'и'
			w.forms[fm.PL | fm.INS | size] = lemma + 'ми'
			w.forms[fm.PL | fm.ADP | size] = lemma + 'х'

	elif decl == 2:
		if gender == "mas":
			if end == 'ь':
				w.forms[fm.PL | fm.NOM | size] = lemma[:-1] + 'и'
				w.forms[fm.PL | fm.GEN | size] = lemma[:-1] + 'ей'
				w.forms[fm.PL | fm.DAT | size] = lemma[:-1] + 'ям'
				w.forms[fm.PL | fm.ACC | size] = lemma[:-1] + 'и'
				w.forms[fm.PL | fm.INS | size] = lemma[:-1] + 'ями'
				w.forms[fm.PL | fm.ADP | size] = lemma[:-1] + 'ях'

			else:
				w.forms[fm.PL | fm.NOM | size] = lemma + final[7]
				w.forms[fm.PL | fm.GEN | size] = lemma + final[8]
				w.forms[fm.PL | fm.DAT | size] = lemma + 'ам'
				w.forms[fm.PL | fm.ACC | size] = lemma + final[7]
				w.forms[fm.PL | fm.INS | size] = lemma + 'ами'
				w.forms[fm.PL | fm.ADP | size] = lemma + 'ах'

		else:
			w.forms[fm.PL | fm.NOM | size] = lemma[:-1] + final[2]
			w.forms[fm.PL | fm.GEN | size] = lemma[:-1] + 'ей'
			w.forms[fm.PL | fm.DAT | size] = lemma[:-1] + final[2] + 'м'
			w.forms[fm.PL | fm.ACC | size] = lemma[:-1] + final[2]
			w.forms[fm.PL | fm.INS | size] = lemma[:-1] + final[2] + 'ми'
			w.forms[fm.PL | fm.ADP | size] = lemma[:-1] + final[2] + 'х'

	elif decl == 3:
		w.forms[fm.PL | fm.NOM | size] = lemma[:-1] + 'и'
		w.forms[fm.PL | fm.GEN | size] = lemma[:-1] + 'ей'
		w.forms[fm.PL | fm.DAT | size] = lemma[:-1] + final[6] + 'м'
		w.forms[fm.PL | fm.ACC | size] = lemma[:-1] + 'и'
		w.forms[fm.PL | fm.INS | size] = lemma[:-1] + final[6] + 'ми'
		w.forms[fm.PL | fm.ADP | size] = lemma[:-1] + final[6] + 'х'

	if "animated" in w.specs:
		w.forms[fm.PL | fm.ACC | fm.NRM] = w.forms[fm.PL | fm.GEN | fm.NRM]


def incline_vars_get(w, lemma):
	end = lemma[-1]
	final = ['ы', 'е', 'а', 'у', 'ом', 'ом', 'я', 'ы', 'ов']
	if len(lemma) > 1:
		if lt.is_rulei(lemma[-2]):
			final[0] = 'и'

		if lt.is_vowel(lemma[-2]):
			final[1] = 'и'

		if lt.is_vowel(lemma[-2]):
			final[2] = 'я'
			final[3] = 'ю'
			final[4] = 'ем'

		if lt.is_hushing(lemma[-2]):
			final[6] = 'а'

		if lt.is_hushing(lemma[-1]):
			final[7] = 'и'
			final[8] = 'ей'

		if end == 'е':
			final[4] = 'ем'

		if end == 'щ':
			final[5] = 'ем'

	return (w.specs["gender"], end, final)
