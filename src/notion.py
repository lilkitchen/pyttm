#
# notion.py
#

import options
import sexp

notions = {}

class Notion:
	def __init__(self, name=None):
		self.name = name
		self.specs = {}

	def string(self, indent=0):
		s = ''
		if self.name:
			s += '"' + self.name + '"\n'

		# TODO: unnamed recursive display

		for k in self.specs:
			spec = self.specs[k]
			if isinstance(spec, list):
				for i in range(indent):
					s += '\t'
				s += k + ': '
				for e in spec:
					s += '"' + e.name + '" '
				s += '\n'

			elif isinstance(spec, bool):
				s += "\t--" + k

			elif isinstance(spec, str):
				s += k + ': ' + '"' + spec + '"' + '\n'

		return s

	def display(self, indent=0):
		print(self.string(indent=indent))

def init():
	sx, err = sexp.load_file("../data/notions")
	if err:
		return err

	for sub in sx:
		if not isinstance(sub, list) or len(sub) == 0:
			return "Wrong notion syntax: " + sub

		if sub[0] in notions:
			return "Notion duplicate: " + sub

		n = Notion(sub[0])
		for m in sub[1:]:
			if not isinstance(m, list) or len(m) < 2:
				return "Wrong notion syntax: " + m + " in " + str(sub)

			if m[0] == sexp.DEF:
				n.specs[m[1]] = m[2]

			elif m[0] == sexp.FLAGS:
				for f in m[1:]:
					n.specs[f] = True

			else:
				return "Wrong notion syntax: " + m + " in " + str(sub)

		notions[sub[0]] = n

	for key in notions:
		n = notions[key]
		for k in n.specs:
			if isinstance(n.specs[k], list):
				ls = []
				for name in n.specs[k]:
					if name not in notions:
						if not options.quiet:
							print("Notion \"" + name + "\" not found")
						continue

					ls.append(notions[name])

				n.specs[k] = ls
