# -*- coding: utf-8 -*-
from chatterbot .trainers import ListTrainer
from chatterbot import ChatBot
print("====" * 20)
print('''__  ____   __  ____   ___ _____
|  \/  \ \ / / | __ ) / _ \_   _|
| |\/| |\ V /  |  _ \| | | || |
| |  | | | |   | |_) | |_| || |
|_|  |_| |_|   |____/ \___/ |_|''')
print("Este programa é um bot que aprende com suas palavras digitadas na lista ele ira treinar elas com base em suas conversas, digite a quantidade para quantas palavras você quer treinar com ele, e depois da quantidade ele ira verificar as palavras que cosrepondem. OBS: é importante vc coloca-las em sequencia assim ele ira ter uma conversa com contexto. EXP: 'oi', 'ola', 'como vai?', 'bem' ")
print("====" * 20)

bot = ChatBot(input("nome do seu bot: "))
i = 0
conv = []
quantidade = input("digite a quantidade de palavras que você quer para adicionar a lista: ")
while i < int(quantidade):
	i = i + 1
	b = input("digite as palavras que o bot vai treinar: ")
	conv.append(b)
bot.set_trainer(ListTrainer)
bot.train(conv)
while True:
	quest = input("Você: ")
	response = bot.get_response(quest)
	print("Pedro Bot: ", response)