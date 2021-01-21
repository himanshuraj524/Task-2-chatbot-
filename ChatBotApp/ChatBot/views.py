from django.shortcuts import render, HttpResponse

import json # json for converting the reply into json form to return to the API request.
import datetime  # this is for date and time related queries.

from ChatBot.models import UserMessage #importing the model for storing the user messages.

# Create your views here.
def home(request):
    #This is to load the home page of the chat bot.
    return render(request, 'home.html')


def wishMe(messageData, wishes):
    """
    This function will wish the user based on the time zone.
    """
    if messageData in wishes:
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            resp = ("good morning.")
        elif 12 <= hour < 18:
            resp = ("good afternoon.")
        else:
            resp = ("good evening.")
    BotReply = resp
    return BotReply


def Response(request):
    """
    This function will store the userQuery in the database and deliver the appropriate response.
    """
    messageData = json.load(
        request)['message']  # access the user query from the fetch API request.

    # storing the query in the database.
    Query = UserMessage(UserQuery=messageData)
    Query.save()  # using save function to save the data in database.

    # converting the query into lowercase for easier operation.
    messageData = messageData.lower()

    # Algorithm for BotReply.
    try:
        wishes = ['good morning', 'good afternoon', 'good evening'] #user wishes.
        Greetinp = {
                    'hi':'hello :)',
                    'hello':'hi :)',
                    'who are you':'i am your chatbot :)',
                    'can you help me':'i am here to help you.',
                    'thank you':'Your welcome :)',
                    'what can you do':'i am here to help you to take the precautions against COVID-19 virus.',
                    'bye':'Okay! we will meet soon.'
                    }  #greet to user.

        Covidinp = ['what is covid', 'what is coronavirus',
                    'what is covid19', "covid", "covid19", "coronavirus", "corona"]  #covid related questions.

        if messageData in wishes:
            #wishes the user based on user message.
            BotReply = wishMe(messageData, wishes)

        elif messageData in Greetinp:
            #greet the user based on user message.
            BotReply = Greetinp[messageData]

        elif messageData in Covidinp:
            # if user asks about corona, user will get the below response.
            BotReply = "A coronavirus is a kind of common virus that causes an infection in your nose, sinuses, or upper throat. Most coronaviruses aren't dangerous.In early 2020, after a December 2019 outbreak in China, the World Health Organization identified SARS-CoV-2 as a new type of coronavirus. The outbreak quickly spread around the world.COVID-19 is a disease caused by SARS-CoV-2 that can trigger what doctors call a respiratory tract infection. It can affect your upper respiratory tract (sinuses, nose, and throat) or lower respiratory tract (windpipe and lungs).It spreads the same way other coronaviruses do, mainly through person-to-person contact. Infections range from mild to deadly."
        
        else:
            # if any error occured the this response will sended with the reply.
            BotReply = "Wrong input!"

    except Exception as e:
        print(e)
        BotReply = "Sorry!"

    #These params will send to the front end by converting them into json format.
    Params = {
        'BotReply': BotReply.capitalize(), #this is the bot reply
    }

    ReplyData = json.dumps(Params) #converting the params into json.

    return HttpResponse(ReplyData)
