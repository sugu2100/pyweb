from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    season = '겨울'
    return render(request, 'board/question_list.html',
                  {'season':season})
    #return HttpResponse("pyweb 사이트 입니다.")
