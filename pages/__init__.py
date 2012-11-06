import os

for i in os.listdir(os.getcwd()):
	if i[-3:] == '.py':
		print i	
