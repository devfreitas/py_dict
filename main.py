import os
os.system("cls" if os.name == "nt" else "clear")

aluno = {
    "nome" : "Carlos",
    "idade" : 21,
    "curso" : "TDS"
}

# print(aluno["nome"])
# print(aluno.get("cel"))
# print(aluno.get("curso"))

# aluno["idade"] = input("Idade: ")
# print(aluno)

# print(aluno)
aluno["nota"] = 9.5
# print(aluno)

# print(aluno)
# aluno["nome"] = "Edson"
# print(aluno)

# os.system("cls")
# print(aluno)
# aluno.pop("curso")
# print(aluno)

# os.system("cls")
# print(aluno)
# del aluno["curso"]
# print(aluno)

# print(aluno)
# print(aluno.get("curso"))
# print(aluno.keys())
# print(aluno.values())
# print(aluno.items())
# aluno.update({"nome":"ana"})
# print(aluno)
# print(aluno.pop("curso"))

# os.system("cls")
# print(aluno)
# aluno.clear()
# print(aluno)
# # aluno.pop("nome")
# # del aluno["nome"]

# print(aluno)
# aluno.clear()
# print(aluno)
# del aluno
# print(aluno)

for n, k in enumerate(aluno.keys()):
    print(f"Campo {n} : {k}")


for n, v in enumerate(aluno.values()):
    print(f"Campo {n} : {v}")


for n, i in aluno.items():
    print(f"Campo {n} : {i}")

aluno.pop("nome")
print()
for k, v in aluno.items():
    print(f"{k} : {v}")



