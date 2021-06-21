from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
'''def index(request):

    #data_atual = date.today()
    #return HttpResponse(data_atual)
    return render(request, "index.html")
'''
def index (request):
    date_srt = datetime.now()
    html = '''
    <html>
        <head><title>Avaliação SOCPS II</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <h2>Bruno Ribeiro Braga Silva Freire</h2>
            <h3>Data e hora: %s</h3>
        </body>
    </html>
    ''' % date_srt
    return HttpResponse(html)