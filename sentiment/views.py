
from django.http import HttpResponse , JsonResponse
#from.models import Product , User


from django.template import loader
import logging
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from textblob import TextBlob
from django.shortcuts import render

x ={}

def index(request):
    template = loader.get_template('sentiment/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def indexpage(request):
	return render(request, 'sentiment/indexpage.html')

def home(request):
    template = loader.get_template('sentiment/home.html')
    context={}
    return HttpResponse(template.render(context,request))

def hist(request):
    global x
    template = loader.get_template('sentiment/hist.html')
    context={'x':x}
    logger.error(context)
    return HttpResponse(template.render(context,request))

logger = logging.getLogger(__name__)

@csrf_exempt
def analysis(request):
    sentence = request.GET.getlist('strr')
    logger.error(sentence)
    global x
    pos =0
    neg =0
    neu = 0
    sentence = ["product is good but is dull"]
    
    for word in sentence:
        blob = TextBlob(word)
        #logger.error(word)
        #logger.error(blob.sentiment.polarity)
        if blob.sentiment.polarity > 0:
            pos = pos+blob.sentiment.polarity
        elif blob.sentiment.polarity < 0:
            neg = neg+blob.sentiment.polarity
        else:
            neu = neu+blob.sentiment.polarity

    if (abs(pos + neg) < 0.5 ):
        a = {"name": neu, "b": "Neutral", "score": abs(pos+neg), "pos": pos, "neg": neg, "neu": neu}
    elif(pos>abs(neg) and pos>neu ):
        a = {"name":pos,"b":"Positive", "score": pos,"pos":pos,"neg":neg,"neu":neu}
    elif(abs(neg)>pos and abs(neg)>neu):
        a ={"name":neg,"b":"Negative", "score": neg ,"pos":pos,"neg":neg,"neu":neu}

    logger.error(pos)
    logger.error(neg)
    logger.error(neu)
    logger.error(abs(neg))

    x = {"pos":pos,"neg":abs(neg),"neu":abs(pos+neg)}
    return JsonResponse(a)
