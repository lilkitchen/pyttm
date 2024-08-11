#
# bot.py
#

import asyncio
import aiogram
from aiogram import types, F
from aiogram.filters import Command

import notion
import parser
import tok
import ttm
import word

TALK = 0
NOTION = 1
FIND = 2
WORD = 3
TOKENIZE = 4
PARSE = 5

file = open("../token", "r")
token = file.readline().rstrip()
file.close()

bot = aiogram.Bot(token=token)
dp = aiogram.Dispatcher()

chats = {}

@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
	await msg.answer("PyTTM is now listening to you")

@dp.message(Command("talk"))
async def cmd_talk(msg: types.Message):
	chats[msg.chat.id] = TALK
	await msg.answer("Привет")

@dp.message(Command("notion"))
async def cmd_notion(msg: types.Message):
	chats[msg.chat.id] = NOTION
	await msg.answer("Type a notion to look for")

@dp.message(Command("find"))
async def cmd_find(msg: types.Message):
	chats[msg.chat.id] = FIND
	await msg.answer("Type a literal to look for")

@dp.message(Command("word"))
async def cmd_word(msg: types.Message):
	chats[msg.chat.id] = WORD
	await msg.answer("Type a word to look for")

@dp.message(Command("tokenize"))
async def cmd_tokenize(msg: types.Message):
	chats[msg.chat.id] = TOKENIZE
	await msg.answer("Type a sentense to tokenize")

@dp.message(Command("parse"))
async def cmd_parse(msg: types.Message):
	chats[msg.chat.id] = PARSE
	await msg.answer("Type a sentense to parse")

@dp.message(F.text)
async def text(msg: types.Message):
	state = TALK
	if msg.chat.id in chats:
		state = chats[msg.chat.id]

	if state == TALK:
		reply = ttm.tell(msg.text)
		if reply:
			await msg.answer(reply)

	elif state == NOTION:
		if msg.text in notion.notions:
			await msg.answer(notion.notions[msg.text].string())

	elif state == FIND:
		s = ''
		if msg.text in word.forms:
			for w in word.forms[msg.text]:
				s += w.string()

		if s:
			await msg.answer(s)

	elif state == WORD:
		w = word.find(msg.text)
		if w:
			await msg.answer(w.string())

	elif state == TOKENIZE:
		s = ''
		tokens = tok.tokenize(msg.text)
		for t in tokens:
			s += t.string()

		if s:
			await msg.answer(s)

	elif state == PARSE:
		s = ''
		treats = parser.parse(msg.text)
		for t in treats:
			for n in t:
				s += n.string()

		if s:
			await msg.answer(s)

async def main():
	err = ttm.init()
	if err:
		print(err)
		return

	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())
