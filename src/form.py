#
# form.py
#

import sexp

SG = 0x1
PL = 0x2

NUMBER = SG | PL

MAS = 0x4
FEM = 0x8
COM = 0x10

GENDER = MAS | FEM | COM

NOM = 0x20
GEN = 0x40
DAT = 0x80
ACC = 0x100
INS = 0x200
ADP = 0x400

CASE = NOM | GEN | DAT | ACC | INS | ADP

PRES = 0x800
PAST = 0x1000
FUTR = 0x2000

TENSE = PRES | PAST | FUTR

INF = 0x4000
IMP = 0x8000
FST = 0x10000
SEC = 0x20000
TRD = 0x40000

PERSON = INF | IMP | FST | SEC | TRD

POS = 0x80000
CMP = 0x100000
SUP = 0x200000

COMPARISON = POS | CMP | SUP

IMPF = 0x400000
PF = 0x800000

ASPECT = IMPF | PF

ACT = 0x4000000
PAS = 0x8000000
RFX = 0x2000000

VOICE = ACT | PAS | RFX

NRM = 0x10000000
DIM = 0x20000000
AUG = 0x40000000

SIZE = NRM | DIM | AUG

FULL = 0x80000000
SHRT = 0x100000000

LENGTH = FULL | SHRT

LABELS = {
	"sg": SG,
	"singular": SG,
	"pl": PL,
	"plural": PL,
	"mas": MAS,
	"masculine": MAS,
	"fem": FEM,
	"feminine": FEM,
	"com": COM,
	"common": COM,
	"nom": NOM,
	"nominative": NOM,
	"gen": GEN,
	"genitive": GEN,
	"dat": DAT,
	"dative": DAT,
	"acc": ACC,
	"accusative": ACC,
	"ins": INS,
	"instrumental": INS,
	"adp": ADP,
	"adpositional": ADP,
	"pres": PRES,
	"present": PRES,
	"past": PAST,
	"futr": FUTR,
	"future": FUTR,
	"inf": INF,
	"infinitive": INF,
	"imp": IMP,
	"imperative": IMP,
	"fst": FST,
	"first": FST,
	"1st": FST,
	"sec": SEC,
	"2nd": SEC,
	"second": SEC,
	"trd": TRD,
	"3rd": TRD,
	"third": TRD,
	"pos": POS,
	"positive": POS,
	"cmp": CMP,
	"comparative": CMP,
	"sup": SUP,
	"superlative": SUP,
	"impf": IMPF,
	"imperfect": IMPF,
	"pf": PF,
	"perfect": PF,
	"rfx": RFX,
	"reflexive": RFX,
	"act": ACT,
	"active": ACT,
	"pas": PAS,
	"pass": PAS,
	"passive": PAS,
	"nrm": NRM,
	"norm": NRM,
	"normal": NRM,
	"dim": DIM,
	"diminutive": DIM,
	"aug": AUG,
	"augmentative": AUG,
	"full": FULL,
	"shrt": SHRT,
	"short": SHRT,
}

def read(sx):
	if not isinstance(sx, list) or sx[0] != sexp.FORM:
		return

	form = 0
	for sub in sx:
		if sub in LABELS:
			form |= LABELS[sub]

	return form

def string(form, e='\n'):
	s = '(@'
	printed = 0

	for k in LABELS:
		if form & LABELS[k] and not printed & LABELS[k]:
			s += ' ' + k
			printed |= LABELS[k]

	s += ')' + e

	return s

def display(form, e='\n'):
	print(string(form, e))
