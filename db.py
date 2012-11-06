import sqlite3

def connect_db(path):
	g.db = sqlite3.connect(path)
	g.db.row_factory = sqlite3.Row()

def create_char_database(c):
	c.executescript(
	"""
	CREATE TABLE char (
		name TEXT PRIMARY KEY,
		relative TEXT,
		town TEXT,
		area TEXT,
		reward REAL);
	CREATE TABLE bonnus (
		id INTEGER PRIMARY KEY,
		char TEXT,
		bonus_type TEXT,
		bonus REAL);
	CREATE TABLE phrases(
		id INTEGER PRIMARY KEY,
		char TEXT, 
		type TEXT,
		phrase TEXT);
	CREATE TABLE bobots(
		id INTEGER PRIMARY KEY,
		name TEXT,
		char TEXT);
	CREATE TABLE parts(
		id INTEGER PRIMARY KEY,
		bobot INTEGER,
		part TEXT,
		level INTEGER);
	"""
	)
	
def populate_char_database(c):
	char_list = [
	('Lilly', 'Ms. Honey','SquirrelTown', 'School', 'Agility', 0.03,"And isn't he pretty, too?", "Mine is still the cutest.",10, 'Rodent','Push')
	] 
	c.executescript(
	"""
	INSERT INTO char 
	"""
	)	

db = sqlite3.connect(path)
c = db.cursor()

create_char_database(c)
