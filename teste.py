



def rodar():
	print 'r'

def cair():
	print 'c'

def pular():
	print 'p'

status = 'chao'


comandos = {
		'rodar':rodar,
		'voando':cair,
		'chao': pular,
	}
comandos[status]()



