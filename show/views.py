# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
        friends = ['tama', 'koma', 'pochi', 'ben', 'tora']
        return render_to_response('index.html', {'friends':friends})
def tama(request):
        return render_to_response('tama.html')
def koma(request):
        return render_to_response('koma.html')
def pochi(request):
        return render_to_response('pochi.html')
def ben(request):
        return render_to_response('ben.html')
def tora(request):
        return render_to_response('tora.html') 
                                  