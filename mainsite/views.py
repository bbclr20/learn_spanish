from django.shortcuts import render
from .models import Vocab
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def homepage(request):
    now = datetime.now()
    class_choices = Vocab.classes_choices
    template = loader.get_template("homepage.html")
    html = template.render(locals())
    return HttpResponse(html)

def vocabulary(request, class_choice):
    classes = Vocab.lookup_dict[class_choice]
    vocabs = Vocab.objects.all().filter(classes=classes)
    template = loader.get_template("vocabulary.html")
    html = template.render(locals())
    return HttpResponse(html)
