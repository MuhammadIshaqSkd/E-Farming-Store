from django.shortcuts import render
import pyttsx3
from django.http import HttpResponse
#-------------------  Hotel Views.py.................

# Create your views here.
def index(request):
    return render(request, 'index.html')

def complaindesk(request):
    # engine = pyttsx3.init()
    #
    # engine = pyttsx3.init()
    #
    # rate = engine.getProperty("rate")
    # engine.setProperty("rate", 140)
    # volume = engine.getProperty("volume")
    # engine.setProperty("volume", 1)
    #
    # voices = engine.getProperty("voices")
    # engine.setProperty("voice", voices[1].id)
    #
    # engine.say("Hello! Sir submit your complaint below.")
    #
    # engine.runAndWait()
    return render(request, 'compaindesk.html')

def contactUS(request):

    d = 'name'
    return render(request, 'contactus.html',{'d':d})