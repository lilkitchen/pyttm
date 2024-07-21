#
# sexp.py
#

DEF = ":"
FLAGS = "--"
FORM = "@"

class Context:
	def __init__(self, file):
		self.file = file
		self.pos = 0
		self.err = None
		self.line = 0

	def getc(self):
		self.pos = self.file.tell()
		c = self.file.read(1)
		if c == '\n':
			self.line += 1

		return c

	def ungetc(self):
		self.file.seek(self.pos)

	def linefeed(self):
		self.line += 1

	def err_get(self):
		return ">>> " + self.err + " at line " + self.line

def load_file(path):
	file = open(path, 'r', encoding="utf-8")
	if not file:
		return (None, "Failed to open a file")

	ctx = Context(file)

	lst = scan_list(ctx)
	if ctx.err:
		return (None, ctx.err_get())

	file.close()

	return (lst, None)

def scan_list(ctx):
	lst = []
	while True:
		obj = scan_any(ctx)
		if ctx.err:
			return None

		if obj is None:
			break

		lst.append(obj)

	return lst

def scan_any(ctx):
	while True:
		c = ctx.getc()
		if c == '\n' or c == ' ' or c == '\t':
			continue

		elif c == '#':
			scan_comment(ctx)

		else:
			break

	if not c:
		return None

	elif c == '(':
		return scan_list(ctx)

	elif c == ')':
		return None

	elif c == '"':
		return scan_str(ctx)

	elif c == '!':
		obj = scan_any(ctx)
		if ctx.err:
			return None

		return ["not", obj]

	elif c == '-':
		return scan_flags(ctx)

	else:
		ctx.ungetc()
		return scan_sym(ctx)

def scan_str(ctx):
	str = ""
	while True:
		c = ctx.getc()
		if not c:
			ctx.err = "Unexpected string end"
			return None

		if c == '"':
			return scan_def(ctx, str)

		if c == '\\':
			c = ctx.getc()
			if c == '\n':
				continue

			elif c == '\\':
				str += c

			elif c == 'n':
				str += '\n'

			elif c == 't':
				str += '\t'

			else:
				ctx.err = "Wrong escape sequence"
				return None

		else:
			str += c

def scan_sym(ctx):
	sym = ""
	while True:
		c = ctx.getc()
		if not c:
			return sym

		if c == '\n' or c == ' ' or c == '\t' or \
			c == '(' or c == ')' or c == ':':
			ctx.ungetc()
			return scan_def(ctx, sym)

		sym += c

def scan_def(ctx, key):
	c = ctx.getc()
	if c == ':':
		obj = scan_any(ctx)
		if ctx.err:
			return None

		if obj is None:
			ctx.err = "Wrong use of def syntax"
			return None

		return [DEF, key, obj]

	ctx.ungetc()

	return key

def scan_flags(ctx):
	c = ctx.getc()
	if c == '-':
		c = ctx.getc()
		if c == ' ' or c == '\n' or c == '\t':
			return FLAGS

		elif c == '(' or c == ')' or c == ':':
			ctx.err = "Wrong flag syntax"
			return

		else:
			ctx.ungetc()
			obj = scan_any(ctx)
			if ctx.err:
				return

			return [FLAGS, obj]

	elif c == '\n' or c == '\t' or c == ' ':
		return '-'

	else:
		obj = [FLAGS]
		while True:
			if c == ' ' or c == '\n' or c == '\t':
				return obj

			elif c == '(' or c == ':':
				ctx.err = "Wrong flag syntax"
				return

			else:
				obj.append(c)
				c = ctx.getc()

def scan_comment(ctx):
	while True:
		c = ctx.getc()
		if not c or c == '\n':
			break
