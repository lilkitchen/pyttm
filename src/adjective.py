#
# adjective.py
#

import form as fm

def load(w):
	end = w.lemma[-2]

	if "decl" not in w.specs:
		if end == 'ы':
			w.specs["decl"] = "hard"

		elif end == 'и':
			w.specs["decl"] = "soft"

		else:
			w.specs["decl"] = "mixed"

	f = fm.SG | fm.POS | fm.NRM | fm.FULL

	w.forms[f | fm.MAS | fm.NOM] = w.lemma

	if w.specs["decl"] == "hard":
		w.forms[f | fm.MAS | fm.GEN] = w.lemma[:-2] + 'ого'
		w.forms[f | fm.MAS | fm.DAT] = w.lemma[:-2] + 'ому'
		w.forms[f | fm.MAS | fm.ACC] = w.lemma
		w.forms[f | fm.MAS | fm.INS] = w.lemma[:-2] + 'ым'
		w.forms[f | fm.MAS | fm.ADP] = w.lemma[:-2] + 'ом'

		w.forms[f | fm.FEM | fm.NOM] = w.lemma[:-2] + 'ая'
		w.forms[f | fm.FEM | fm.GEN] = w.lemma[:-2] + 'ой'
		w.forms[f | fm.FEM | fm.DAT] = w.lemma[:-2] + 'ой'
		w.forms[f | fm.FEM | fm.ACC] = w.lemma[:-2] + 'ую'
		w.forms[f | fm.FEM | fm.INS] = w.lemma[:-2] + 'ой'
		w.forms[f | fm.FEM | fm.ADP] = w.lemma[:-2] + 'ой'

		w.forms[f | fm.COM | fm.NOM] = w.lemma[:-2] + 'ое'
		w.forms[f | fm.COM | fm.GEN] = w.lemma[:-2] + 'ого'
		w.forms[f | fm.COM | fm.DAT] = w.lemma[:-2] + 'ому'
		w.forms[f | fm.COM | fm.ACC] = w.lemma[:-2] + 'ое'
		w.forms[f | fm.COM | fm.INS] = w.lemma[:-2] + 'ым'
		w.forms[f | fm.COM | fm.ADP] = w.lemma[:-2] + 'ом'

	elif w.specs["decl"] == "soft":
		w.forms[f | fm.MAS | fm.GEN] = w.lemma[:-2] + 'его'
		w.forms[f | fm.MAS | fm.DAT] = w.lemma[:-2] + 'ему'
		w.forms[f | fm.MAS | fm.ACC] = w.lemma
		w.forms[f | fm.MAS | fm.INS] = w.lemma[:-2] + 'им'
		w.forms[f | fm.MAS | fm.ADP] = w.lemma[:-2] + 'ем'

		w.forms[f | fm.FEM | fm.NOM] = w.lemma[:-2] + 'яя'
		w.forms[f | fm.FEM | fm.GEN] = w.lemma[:-2] + 'ей'
		w.forms[f | fm.FEM | fm.DAT] = w.lemma[:-2] + 'ей'
		w.forms[f | fm.FEM | fm.ACC] = w.lemma[:-2] + 'юю'
		w.forms[f | fm.FEM | fm.INS] = w.lemma[:-2] + 'ей'
		w.forms[f | fm.FEM | fm.ADP] = w.lemma[:-2] + 'ей'

		w.forms[f | fm.COM | fm.NOM] = w.lemma[:-2] + 'ее'
		w.forms[f | fm.COM | fm.GEN] = w.lemma[:-2] + 'его'
		w.forms[f | fm.COM | fm.DAT] = w.lemma[:-2] + 'ему'
		w.forms[f | fm.COM | fm.ACC] = w.lemma[:-2] + 'ее'
		w.forms[f | fm.COM | fm.INS] = w.lemma[:-2] + 'им'
		w.forms[f | fm.COM | fm.ADP] = w.lemma[:-2] + 'ем'

	elif w.specs["decl"] == "mixed":
		w.forms[f | fm.MAS | fm.GEN] = w.lemma[:-2] + 'ого'
		w.forms[f | fm.MAS | fm.DAT] = w.lemma[:-2] + 'ому'
		w.forms[f | fm.MAS | fm.ACC] = w.lemma
		w.forms[f | fm.MAS | fm.INS] = w.lemma[:-2] + 'им'
		w.forms[f | fm.MAS | fm.ADP] = w.lemma[:-2] + 'ом'

		w.forms[f | fm.FEM | fm.NOM] = w.lemma[:-2] + 'ая'
		w.forms[f | fm.FEM | fm.GEN] = w.lemma[:-2] + 'ой'
		w.forms[f | fm.FEM | fm.DAT] = w.lemma[:-2] + 'ой'
		w.forms[f | fm.FEM | fm.ACC] = w.lemma[:-2] + 'ую'
		w.forms[f | fm.FEM | fm.INS] = w.lemma[:-2] + 'ой'
		w.forms[f | fm.FEM | fm.ADP] = w.lemma[:-2] + 'ой'

		w.forms[f | fm.COM | fm.NOM] = w.lemma[:-2] + 'ое'
		w.forms[f | fm.COM | fm.GEN] = w.lemma[:-2] + 'ого'
		w.forms[f | fm.COM | fm.DAT] = w.lemma[:-2] + 'ому'
		w.forms[f | fm.COM | fm.ACC] = w.lemma[:-2] + 'ое'
		w.forms[f | fm.COM | fm.INS] = w.lemma[:-2] + 'им'
		w.forms[f | fm.COM | fm.ADP] = w.lemma[:-2] + 'ом'

	# TODO: comparative, short, diminutive, etc.
	# TODO: adverbs such as тихо/тише
