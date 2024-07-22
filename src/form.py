#
# form.py
#

import sexp

SG = 0x1
PL = 0x2

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

IMPF = 0x400000
PF = 0x800000

NRFX = 0x1000000
RFX = 0x2000000

ACT = 0x4000000
PASS = 0x8000000

NORM = 0x10000000
DIM = 0x20000000
AUG = 0x40000000

SIZE = NORM | DIM | AUG

FULL = 0x80000000
SHRT = 0x100000000

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
	"fut": FUTR,
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
	"nrfx": NRFX,
	"nonreflexive": NRFX,
	"rfx": RFX,
	"reflexive": RFX,
	"act": ACT,
	"active": ACT,
	"pass": PASS,
	"passive": PASS,
	"norm": NORM,
	"normal": NORM,
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

def display(form, e='\n'):
	printed = 0

	print('(@ ', end='')

	for k in LABELS:
		if form & LABELS[k] and not printed & LABELS[k]:
			print(k, end=' ')
			printed |= LABELS[k]

	print(')', end=e)
