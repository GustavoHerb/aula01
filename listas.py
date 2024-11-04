#                           EXERCICIO 1

# lista_numero = [1, 2, 3, 4, 5]

# for i in lista_numero:
#     print(i)
  
#                            EXERCICIO 2
# lista_vogal = ["a", "e", "i", "o", "u"]

# for indice, vogal in enumerate(lista_vogal, 
# start=1 ):
#    print(f"vogal {indice}: {vogal}")


#       #                    EXERCICIO 3

# lista_classes = ["sla", 2, True, 3.4, "anham"]
# lista_classes.append("pppp")

# for indice, item in enumerate(lista_classes, start=1):
#   print(f"O item é: {indice}: {item} - O tipo é: {type(item).__name__}")

# lista_de_compra = [
#     "Macarrão",
#     "Carne Móida",
#     "Linguiça Calabresa",
#     "Molho de tomate"

# ]

# print("LISTA DE COMPRAS", end= '\n\n')


# #pecorrendo a lista de compras
# for item in lista_de_compra: 
#   print("[ ]", item)

# pro = int(input("Digite o numero do convidado para pesquisar."))

# lista_convidados = ("Rogério,", "Roberto,", "Rayssa,", "Santiago,", "Raquel,", "Rubens,", "Renata,", "Ricardo,", "Rita,", "Raul.")
# procurado = lista_convidados - 1 [pro + 1]

# for i in lista_convidados:
#   if i == procurado:
#     print(i)



# convidados = [
#     "Carlos", "Ana", "João", "Mariana", "Pedro", "Laura", "Lucas", "Fernanda", "Roberto", "Camila"
# ]

# convites = (
#     "A34B89", "C57Z31", "D92X74", "E81Y65", "F03V28", "G56W49", "H77T12", "J88Q34", "K19L53", "L20M67"
# )

# print("Lista de Convidados: ")
# for i, convidado in enumerate(convidados):
#   print(f"{i + 1}. {convidado}")

# posicao_convidado = int(input("\nDigite o número respectivo do convidado (1 - 10): "))

# if posicao_convidado >= 1 and posicao_convidado <=10:
#   numero_convite = convites[posicao_convidado - 1]
#   print(f"O convite do convidado {convidados[posicao_convidado - 1]} é: {numero_convite}")
# else:
#   print("Número digitado invalido. Por favor, tente novamente.")


# ATIVIDADE 4

# palestrantes = (
#     ("Alice Silva", "Inteligência Artificial", "Universidade de Tecnologia X"),
#     ("Bruno Souza", "Desenvolvimento Web", "Instituto de Tecnologia Y"),
#     ("Carla Mendes", "Segurança Cibernética", "Faculdade de Ciências Z")
# )

# numero = int(input("Digite o número do palestrante (1, 2 ou 3): "))

# if 1 <= numero <= 3:
#     nome, tema, instituicao = palestrantes[numero - 1]
#     print("\nInformações do palestrante selecionado:")
#     print(f"Nome: {nome}")
#     print(f"Tema da palestra: {tema}")
#     print(f"Instituição: {instituicao}")
# else:
#     print("Número inválido. Por favor, digite 1, 2 ou 3.")


#               DESAFIO


# resultados = [
#     ("Equipe A", [10, 15, 20, 25]),
#     ("Equipe B", [14, 18, 22, 26]),
#     ("Equipe C", [12, 17, 21, 24])
# ]


# medias = [(equipe[0], sum(equipe[1]) / len(equipe[1])) for equipe in resultados]

# # Ordenando a lista 'medias' em ordem decrescente com base na média
# medias.sort(key=lambda x: x[1], reverse=True)

# classificacao = medias

# print("Classificação final:")
# for equipe, media in classificacao:
#     print(f"{equipe}: Média de {media:.2f}")
