from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import os
import time
import csv




criador = ChatBot("Noob_BOT")
segundo_treinador = ListTrainer(criador)
for arq in os.listdir("arquivo"):
    chat = open("arquivo/"+arq, 'r', encoding="utf-8").readlines()
    segundo_treinador.train(chat)


treinador = ChatterBotCorpusTrainer(criador, encoding='utf-8')

# treinador.train(
#     "chatterbot.corpus.portuguese"
# )
# treinador.train(
#     "chatterbot.corpus.portuguese.greetings",
#     "chatterbot.corpus.portuguese.conversations",
#     "chatterbot.corpus.portuguese.suggestions"
# )




inicio = time.time()
sair = False
interacoes = 0
print("Caminhos de conversa > Chamados ou Procedimentos\n" + "Tipos de procedimento")
while sair == False:
    if interacoes == 0:
        nome = input("Informe seu Nome: ")

    request = input("Pergunte: ").lower()
    resposta = criador.get_response(request)
    if request == "sair" or request == "obrigado":
        print("Obrigado por utilizar o programa")
        fim = time.time()
        tempo_de_execucao = ("%.2f"%((fim - inicio)))
        sair = True
    else:
        print("Bot resposta: "+ str(resposta))
    interacoes+=1




data = csv.reader(open('dados.csv', 'r'))
entradas = [nome, tempo_de_execucao, interacoes]

with open(r'dados.csv', 'a', newline='') as date:
    writer = csv.writer(date, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(entradas)

    sair = False
    interacoes = 0

