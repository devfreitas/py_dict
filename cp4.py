import os;os.system("cls")

comentarios = [
        "O produto é excelente e muito bom!",
        "Péssimo atendimento. Horrível!",
        "A entrega foi ruim, mas o produto é bom",
        "Ótimo custo-benefício",
        "Não gostei, é horrível"
    ]

def limpar_texto(comentario):
    pontuacoes = [",", "!", ".", "?", ";", ":"]
    texto_limpo = comentario.lower()
    for p in pontuacoes:
        texto_limpo = texto_limpo.replace(p, "")
    return texto_limpo

def filtrar_palavras_uteis(texto, palavras_irrelevantes):
    palavras_do_texto = texto.split()
    palavras_uteis = []
    for palavra in palavras_do_texto:
        if palavra not in palavras_irrelevantes:
            palavras_uteis.append(palavra)
    return palavras_uteis

def classificar_sentimento(palavras, palavras_positivas, palavras_negativas):
    is_positivo = any(p in palavras_positivas for p in palavras)
    is_negativo = any(p in palavras_negativas for p in palavras)
    return is_positivo, is_negativo

def exibir_resumo_analise(positivos, negativos, total_palavras):
    """Exibe o relatório final da análise."""
    print("\n--- Resumo da Análise ---")
    print(f"Quantidade de comentários positivos: {positivos}")
    print(f"Quantidade de comentários negativos: {negativos}")
    print(f"Total de palavras úteis analisadas: {total_palavras}")
    print("---------------------------\n")


def analisar_comentarios(comentarios):
    if not comentarios:
        print("Não há comentários para analisar.\n")
        return
    PALAVRAS_IRRELEVANTES = [
        "o", "a", "os", "as", "um", "uma", "uns", "umas", "de", "da", "do",
        "das", "dos", "em", "no", "na", "nos", "nas", "por", "para", "com",
        "sem", "e", "ou", "mas", "que", "foi", "é", "gostei", "não", "muito"
    ]
    PALAVRAS_POSITIVAS = ["bom", "ótimo", "excelente", "ótima", "boa"]
    PALAVRAS_NEGATIVAS = ["ruim", "péssimo", "horrível", "péssima"]

    positivos = 0
    negativos = 0
    total_palavras_uteis = 0

    print("\n--- Análise de Sentimentos ---")
    for comentario in comentarios:
        texto_limpo = limpar_texto(comentario)

        palavras_uteis = filtrar_palavras_uteis(texto_limpo, PALAVRAS_IRRELEVANTES)
        total_palavras_uteis += len(palavras_uteis)

        is_positivo, is_negativo = classificar_sentimento(
            palavras_uteis, PALAVRAS_POSITIVAS, PALAVRAS_NEGATIVAS
        )

        if is_positivo:
            positivos += 1
            print(f'-> "{comentario}" [CLASSIFICADO COMO POSITIVO]')
        if is_negativo:
            negativos += 1
            if not is_positivo:
                print(f'-> "{comentario}" [CLASSIFICADO COMO NEGATIVO]')

    exibir_resumo_analise(positivos, negativos, total_palavras_uteis)


def exibir_comentarios(comentarios):
    print("\n--- Comentários Cadastrados ---")
    if not comentarios:
        print("Nenhum comentário cadastrado ainda.")
    else:
        for i, comentario in enumerate(comentarios, 1):
            print(f"{i}: {comentario}")
    print("--------------------------------\n")

def adicionar_comentario(comentarios):
    novo_comentario = input("Digite seu comentário sobre o produto: ")
    comentarios.append(novo_comentario)
    print("Comentário adicionado com sucesso!\n")

def main():
    while True:
        print("===== Menu de Gerenciamento de Comentários =====")
        print("1. Exibir comentários")
        print("2. Adicionar novo comentário")
        print("3. Analisar comentários")
        print("4. Sair")
        print("==============================================")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case '1':
                exibir_comentarios(comentarios)
            case '2':
                adicionar_comentario(comentarios)
            case '3':
                analisar_comentarios(comentarios)
            case '4':
                print("Saindo do programa. Até logo!")
                break
            case _:
                print("Opção inválida. Por favor, tente novamente.\n")


main()
