#Booleans
"""
print(10 > 9)

print(10 == 9)

print( 10 < 9)


a = 300
b = 33000

if b > a:
    print("b e maior que a")
else:
    print("b e menor que a")
"""
"""
#A maioria dos valores são verdadeiros
x = "hello"
y = 15
print(bool(x))

print(bool(y))

####################################


"""

#Alguns valores são falsos
"""
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""

"""""
#exercicio
class myclass():
    def __len__(self):
        return 0

myobj = myclass()

print(())


"""""
"""""
#Funções podem retornar um booleano

def myFunction():
    return True

print(myFunction())



def myFunction():
    return False

if myFunction():
    print("Sim")
else:
    print("Nao")

"""""

x = 200

print(isinstance(x, str))