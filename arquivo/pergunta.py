# valor = input().lower()
# valor_novo = valor.split(" ")
#
# print(valor_novo)

import os
import re

# def procura_correspondencia(frase, arquivo):
#
#     palavra_procurada = frase.split(" ")
#     arquivo_de_busca = open(arquivo, 'r', encoding="utf-8")
#     for i in range(len(palavra_procurada)):
#         resultado = re.search(i,arquivo_de_busca)
#
#     return print(resultado.group(0))

# frase = "estou procurando por mudança de endereço"
# frase_separada = frase.split(" ")
# for i in range(len(frase_separada)):
#     print(frase_separada[i])
result = re.search('mudanca de endereço', 'quero fazer uma mudanca de endereço')



print(result.group(0))
# valor = re.search(,"mudanca")
#
# print(valor)


# for arq in os.listdir("arquivo"):
#     chat = open("arquivo/"+arq, 'r').readlines()
#     segundo_treinador.train(chat)

