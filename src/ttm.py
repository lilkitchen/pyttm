#
# ttm.py
#

import notion
import parser
import word

def init():
	err = word.init()
	if err:
		return err

	err = notion.init()
	if err:
		return err

def tell(s):
	t = parser.parse(s)

	return "I don't give a flying fuck about that"
