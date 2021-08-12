# Format - Strings
"""
anos = 25

txt = "meu nome e belmiro, e tenho" + anos

print(txt)

"""
"""
anos = 21
txt = "meu nome e belmiro, e tenho {} anos"
print(txt.format(anos))
"""


quantidade = 3
item  = 234
preco = 456.98
compras = "Eu quero pagar {2}  kz por {0} pecas do item {1}"

print(compras.format(quantidade , item, preco ))