#Variáveis Globais
"""
x = 'incrivel'

def myfunc():
    print('python e ' + x)

myfunc()
"""
"""
x = 'incrivel'

def myfunc():
    x = 'fantastico'
    print('python e ' + x)

print("python e " + x)
myfunc()
"""
#A palavra-chave global

def aluno():
    global nome
    nome = "fantastico"

aluno()
print("python e " + nome)
