# Dicionário
# Coleção desordenada de um par de dados

# sintaxe:
"""
<nome do dicionario> = {
    "<key1>" : <value1>,
    "<key2>" : <value2>,
    "<keyN>" : <valueN>,
}
"""
# Criacao de um dicionario vazio
# l = [] # ou list()
# t = () # ou tuple()
# d = {}
# d = dict()

import os
os.system("cls")

# criando um dicionário com valores
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "TDS",
}

print(aluno)

# Acessando os valores
print(aluno["nome"])
print(aluno.get("cel"))
print(aluno.get("curso"))

# Alterar um value (valor)
print(aluno)
aluno["idade"] = 90
print(aluno)
# aluno["idade"] = int(input("Idade: "))
# print(aluno)

# adicionar nova chave (key)
print(aluno)
aluno["nota"] = 9.5
print(aluno)

#print(aluno)
#aluno["Nome"] = "Edson"
#print(aluno)

# Remover valores
os.system("cls")
print(aluno)
# aluno.pop("curso")
print(aluno)
#del aluno["curso"]
print(aluno)


# Principais métodos
os.system("cls")
print(aluno)
print(aluno.get("curso"))
print(aluno.keys())
print(aluno.values())
print(aluno.items())
aluno.update({"nome":"ana"})
print(aluno)
# print(aluno.pop("curso"))
print(aluno)


os.system("cls")
# print(aluno)
# aluno.clear()
# print(aluno)
# aluno.pop("nome")
# del aluno["nome"]

#print(aluno)
#aluno.clear()
#print(aluno)
#del aluno
#print(aluno)

os.system("cls")
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "TDS",
}

print(aluno)

# Exibindo os campos
for n, k in enumerate(aluno.keys()):
    print(f"Campo {n} : {k}")

print()
# Exibindo os values
for n, v in enumerate(aluno.values()):
    print(f"Valor {n} : {v}")

os.system("cls")
print()
# Exibindo os items
for k, v in aluno.items():
    print(f"{k} : {v}")

# aluno.pop("nome")
print()
for k, v in aluno.items():
    print(f"{k} : {v}")

# BONUS
turma = {
    "aluno1": {"nome": "Joao", "nota": 7.5},
    "aluno2": {"nome": "Maria", "nota": 8},
}

print(turma)
print(turma["aluno2"]["nota"])

x = "BANANA"
x.replace()
