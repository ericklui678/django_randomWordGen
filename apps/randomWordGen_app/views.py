from django.shortcuts import render, redirect
import random
import string

def randomWord():
    word = ""
    for i in range(14):
        word += random.choice(string.letters + string.digits)
    return word

def index(request):
    if request.session.get('attempt') == None:
        request.session['attempt'] = 0

    return render(request, 'randomWordGen_app/index.html')

def generate(request):
    request.session['attempt'] += 1
    request.session['word'] = randomWord()
    return redirect('/')
