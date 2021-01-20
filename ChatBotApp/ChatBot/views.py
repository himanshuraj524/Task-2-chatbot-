from django.shortcuts import render,HttpResponse
import json
# Create your views here.
def home(request):
    return render(request,'home.html')

def Response(request):
    messageData = json.load(request)['message']
    BotReply = "Hello ji"
    Params={
        'UserMessage':messageData,
        'BotReply': BotReply
    }

    ReplyData = json.dumps(Params)

    return HttpResponse(ReplyData)