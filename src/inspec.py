#
# insp.py
#

import readline
import sys

import notion
import options
import parser
import tok
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

	options.quiet = False

	readline.parse_and_bind('"e[A": history-search-backward')
	readline.parse_and_bind('"e[B": history-search-forward')

	print("PyTTM inspection. Type h for help or q for quit")

	while True:
		try:
			cmd = input("> ")
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
			print("h/help\t\t\tShow this text")
			print("talk\t\t\tTalk to TTM")
			print("memory\t\t\tShow memory usage")
			print("notion\t\t\tDisplay specific notion")
			print("notions\t\t\tDisplay all notions")
			print("find [literal]\t\tDisplay all words with literal")
			print("word [word]\t\tDisplay specific word")
			print("words\t\t\tDisplay all words")
			print("tokenize [sentence]\tTokenizer")
			print("parse [sentence]\tParser")
			print("q/quit\t\t\tQuit")

		elif cmd[i] == "talk":
			i += 1
			options.quiet = True
			string_arg(i, cmd, talk)
			options.quiet = False

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
			single_arg(i, cmd, word_display)

		elif cmd[i] == "words":
			for w in word.words:
				w.display()

		elif cmd[i] == "tokenize":
			i += 1
			string_arg(i, cmd, tokenize)

		elif cmd[i] == "parse":
			i += 1
			pass

		elif cmd[i] == 'q' or cmd[i] == "quit" or cmd[i] == "exit":
			return True

		i += 1

def repeat_input(func):
	while True:
		try:
			s = input()
			if not s:
				continue

		except EOFError:
			break

		func(s)

def single_arg(i, cmd, func):
	if i < len(cmd):
		func(cmd[i])

	else:
		repeat_input(func)

def string_arg(i, cmd, func):
	if i < len(cmd):
		s = ''
		for e in cmd:
			s += ' ' + e

		s = s.lstrip()
		func(s)

	else:
		repeat_input(func)

def talk(s):
	print('\n\t' + ttm.tell(s), end='\n\n')

def notion_get(s):
	if s in notion.notions:
		notion.notions[s].display()

def literal_get(s):
	if s in word.forms:
		for w in word.forms[s]:
			w.display()

def word_display(s):
	w = word.find(s)
	if w:
		w.display()

def tokenize(s):
	tokens = tok.tokenize(s)
	for t in tokens:
		t.display()

def parse(s):
	treats = parser.parse(s)
	for t in treats:
		for n in t:
			n.display()

def to_mb(num):
	num = num / 1024 / 1024
	return f'{num:.3f}' + "M"

if __name__ == "__main__":
	main()
