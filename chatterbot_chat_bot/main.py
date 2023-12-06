from chatterbot import ChatBot

# Create object of ChatBot class with Logic Adapter
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'SQLMemoryTerminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'trainingtext.txt')


trainer = ListTrainer(bot)

trainingdata = open(file_path).read().splitlines()
trainer.train(trainingdata)


# from chatterbot.trainers import ChatterBotCorpusTrainer
# corpustrainer = ChatterBotCorpusTrainer(bot)

# corpustrainer.train(
#     'chatterbot.corpus.english'
# )

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)