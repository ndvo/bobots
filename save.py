import os
import re

#TODO: identificar o tipo do dado com regex
#

#Regex patterns to capture the content of the file
#These will be inside the functions that loads the save file
load_regex =  '([\w\d]+)\s?=\s?([\w\d]+ ?|{[\s\S]*?}\s|\[[\s\S]*?\]\s|\([\s\S]*?\)\s)'
dict_regex =  '{[\s\S]*}\s?'
list_regex =  '\[[\s\S]*\]\s?'
tuple_regex = '\([\s\S]*\)\?'

def text_or_number(text):
	try:
		return float(text)
	except ValueError:
		return text.strip()

def text2python(content):
	"""convert the content of the save file to python objects using regex"""
	if re.match(dict_regex, content):
		result = dict(re.findall('([\w\d]+) ?: ?([\w\d\{\}\[\]\(\),: ]+[\w\d\{\}\[\]\(\)])', content.strip()[1:-1]))
	elif re.match(list_regex,content):
		result = [text_or_number(i) for i in content.strip()[1:-1].split(',')]
	elif re.match(tuple_regex,content):
		result = [text_or_number(i) for i in tuple(content.strip()[1:-1].split(','))]
	else:
		result = text_or_number(content)
	return result

def load(filename):
	save_file = open(filename,'r').read()
	m = re.findall(load_regex, save_file)
	return dict(m)

def save(char, place, milestones, money, robots):
	savedfiles = os.listdir('saves')
	filenumber = len([i for i in savedfiles if i[-7:]=='.bobots'])+1
	new_save_name = 'slot%0*d.bobots' % (2, filenumber)
	if new_save_name not in savedfiles:
		new_save_file = open(os.path.join('saves', new_save_name), 'w')
	str_robots = ""
	for i in robots:
		str_robots+="""
"""+str(i)
	save_content = """
char = %s
place = %s
milestones = %s
money = %s
%s
	""" % (	char,
		place,
		milestones,
		money,
		str_robots
		)
	new_save_file.write(save_content)


class Saved_Game():
	def __init__(self, filename):
		from_file = load(filename).items()
		self.bode =5
		for k,v in from_file:
			self.__dict__[k] = text2python(v)

