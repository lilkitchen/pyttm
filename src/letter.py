#
# letter.py
#

def is_vowel(c):
	if c == 'а' or c == 'е' or c == 'ё' or c == 'и' or \
		c == 'о' or c == 'у' or c == 'ы' or c == 'э' or \
		c == 'ю' or c == 'я':
		return True

	return False

def is_hushing(c):
	if c == 'ш' or c == 'щ' or c == 'ч' or c == 'ж':
		return True

	return False

def is_rulei(c):
	if c == 'г' or c == 'ж' or c == 'к' or c == 'х' or \
		c == 'ц' or c == 'ч' or c == 'ш' or c == 'щ':
		return True

	return False
