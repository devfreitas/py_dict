import os
os.system("cls" if os.name == "nt" else "clear")

aluno = {
    "nome" : "Carlos",
    "idade" : 21,
    "curso" : "TDS"
}

print(aluno["nome"])
print(aluno.get("cel"))
print(aluno.get("curso"))