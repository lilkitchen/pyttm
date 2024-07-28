#
# inspect.py
#

import readline
import sys

import notion
import token
import ttm
import word

def main():
	err = ttm.init()
	if err:
		print(err)
		return

	if len(sys.argv) > 1:
		apply(sys.argv[1:])
		return

	readline.parse_and_bind('"e[A": history-search-backward')
	readline.parse_and_bind('"e[B": history-search-forward')

	print("PyTTM inspection. Type h for help or q for quit")

	while True:
		try:
			cmd = input()
			if not cmd:
				continue

		except EOFError:
			break

		if apply(cmd.split()):
			break

def apply(cmd):
	i = 0
	while True:
		if i >= len(cmd):
			return

		if cmd[i] == "h" or cmd[i] == "help":
			print("h/help\t\tShow this text")
			print("memory\t\tShow memory usage")
			print("notion\t\tDisplay specific notion")
			print("notions\t\tDisplay all notions")
			print("find [literal]\t\tDisplay all words with literal")
			print("word [word]\t\tDisplay specific word")
			print("words\t\tDisplay all words")
			print("tokenize [sentence]\t\tTokenizer")
			print("parse [sentence]\t\tParser")
			print("q/quit\t\tQuit")

		elif cmd[i] == "memory":
			mem = {
				"Words:": sys.getsizeof(word.words),
				"Forms:": sys.getsizeof(word.forms),
				"Notions:": sys.getsizeof(notion.notions),
			}
			total = 0
			for k in mem:
				print(k, to_mb(mem[k]))
				total += mem[k]

			print("-----------------")
			print("Total:", to_mb(total))

		elif cmd[i] == "notion":
			i += 1
			single_arg(i, cmd, notion_get)

		elif cmd[i] == "notions":
			for k in notion.notions:
				notion.notions[k].display()

		elif cmd[i] == "find":
			i += 1
			single_arg(i, cmd, literal_get)

		elif cmd[i] == "word":
			i += 1
			single_arg(i, cmd, word_get)

		elif cmd[i] == "words":
			for w in word.words:
				w.display()

		elif cmd[i] == "tokenize":
			i += 1
			if i < len(cmd):
				s = ''
				for e in cmd:
					s += ' ' + e

				s = s.lstrip()
				tokenize(s)

			else:
				while True:
					try:
						s = input()
						if not s:
							continue

					except EOFError:
						break

					tokenize(s)

		elif cmd[i] == "parse":
			i += 1
			pass

		elif cmd[i] == 'q' or cmd[i] == "quit" or cmd[i] == "exit":
			return True

		i += 1

def single_arg(i, cmd, func):
	if i < len(cmd):
		func(cmd[i])

	else:
		while True:
			try:
				s = input()
				if not s:
					continue

			except EOFError:
				break

			func(s)

def notion_get(s):
	if s in notion.notions:
		notion.notions[s].display()

def literal_get(s):
	if s in word.forms:
		for w in word.forms[s]:
			w.display()

def word_get(s):
	for w in word.words:
		if s == w.lemma:
			w.display()

def tokenize(s):
	tokens = token.tokenize(s)
	for t in tokens:
		t.display()

def parse(s):
	pass

def to_mb(num):
	num = num / 1024 / 1024
	return f'{num:.3f}' + "M"

if __name__ == "__main__":
	main()
