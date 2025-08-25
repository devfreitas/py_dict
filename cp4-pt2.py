# Leonardo Herrera Sabbatini - RM562170
# Rafael de Freitas Moraes - RM563210

import os
os.system("cls" if os.name == "nt" else "clear")
tabela = []
dicionario = {}
 
# Função destinada para limpar a tela
def limparTela() -> None:
    os.system("cls" if os.name == "nt" else "clear")

# Início das funções principais
 
# Função para criar o dicionário
def criarDicionario(d: dict) -> None:
    while True:
        limparTela()
        print("=== CRIAR DICIONÁRIO ===")
        campo = input("Digite o nome do campo (ou . para finalizar): ")
        if campo == ".":
            print("Dicionário criado com sucesso!")
            break
        print("Escolha o tipo do campo:")
        print("1 - Texto (Str)")
        print("2 - Inteiro (Int)")
        print("3 - Decimal (Float)")
        tipo = input("Opção: ")
 
        match tipo:
            case "1":
                d[campo] = ""
            case "2":
                d[campo] = 0
            case "3":
                d[campo] = 0.0
            case _:
                print("Tipo inválido! Tente novamente.")
                input("\nPressione ENTER para continuar...")
 
# Função para exibir a estrutura do dicionário
def exibirEstrutura(d: dict) -> None:
    limparTela()
    print("=== ESTRUTURA DO DICIONÁRIO ===")
    if not d:
        print("Nenhuma estrutura criada ainda.")
    else:
        tipos = {str: "Texto", int: "Inteiro", float: "Decimal"}
        for campo, valor in d.items():
            tipo_nome = tipos.get(type(valor), "Desconhecido")
            print(f"{campo:15} -> {tipo_nome}")
    input("\nPressione ENTER para continuar...")
 
# Função para cadastrar os registros
def cadastrarRegistro(tabela: list, estrutura: dict) -> None:
    limparTela()
    print("=== CADASTRAR REGISTRO ===")
    if not estrutura:
        print("Estrutura do dicionário não definida!")
        input("\nPressione ENTER para continuar...")
        return
 
    registro = {}
    for campo, valor in estrutura.items():
        match valor:
            case str():
                registro[campo] = input(f"{campo}: ")
            case int():
                registro[campo] = int(input(f"{campo} (inteiro): "))
            case float():
                registro[campo] = float(input(f"{campo} (decimal): "))
 
    tabela.append(registro)
    print("Registro cadastrado com sucesso")
    input("\nPressione ENTER para continuar...")
 
# Função para exibir todos os registros anteriormente cadastrados
def exibirRegistros(tabela: list) -> None:
    limparTela()
    print("=== REGISTROS CADASTRADOS ===")
    if not tabela:
        print("Nenhum registro encontrado")
    else:
        contador = 1
        for registro in tabela:
            print(f"\nRegistro {contador}")
            for campo, valor in registro.items():
                print(f"{campo:15}: {valor}")
            contador += 1
    input("\nPressione ENTER para continuar...")
 
# Função "main", é a função principal que chama todas as outras funções
def main() -> None:
    while True:
        limparTela()
        print("=== MENU PRINCIPAL ===")
        print("1 - Criar estrutura do dicionário")
        print("2 - Listar estrutura do dicionário")
        print("3 - Cadastrar registro")
        print("4 - Exibir registros")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
 
        match opcao:
            case "1":
                criarDicionario(dicionario)
            case "2":
                exibirEstrutura(dicionario)
            case "3":
                cadastrarRegistro(tabela, dicionario)
            case "4":
                exibirRegistros(tabela)
            case "0":
                break
            case _:
                print("Opção inválida!")
                input("\nPressione ENTER para continuar...")

main()
print("Finalizando...")
