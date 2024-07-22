#
# inspect.py
#

import sys

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
			print("find [literal]\t\tDisplay all words with literal")
			print("word [word]\t\tDisplay specific word")
			print("words\t\tDisplay all words")
			print("q/quit\t\tQuit")

		elif cmd[i] == "memory":
			mem = {
				"Words:": sys.getsizeof(word.words)
			}
			total = 0
			for k in mem:
				print(k, to_mb(mem[k]))
				total += mem[k]

			print("-----------------")
			print("Total:", to_mb(total))

		elif cmd[i] == "find":
			# TODO: if there is no [literal] do read/eval loop
			print("Not implemented yet")
			i += 1

		elif cmd[i] == "word":
			# TODO: if there is no [word] do read/eval loop
			print("Not implemented yet")
			i += 1

		elif cmd[i] == "words":
			word.display()

		elif cmd[i] == 'q' or cmd[i] == "quit" or cmd[i] == "exit":
			return True

		i += 1

def to_mb(num):
	num = num / 1024 / 1024
	return f'{num:.3f}' + "M"

if __name__ == "__main__":
	main()
