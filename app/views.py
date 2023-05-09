from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import *


# Create your views here.

def dummy(request):
    return render(request, 'dummy.html')


# def insert_data(request):
#     # json_data = 'C:\Users\Marvel\Desktop\Project\intern\Scripts\trail\static
#     a = 'C:\\Users\\Marvel\\Desktop\\Project\\intern\\Scripts\\trail\\app\\jsondata.json'
#     with open(a, 'r', encoding='utf-8', errors='replace') as fo:
#         dd= fo.read()
        
#         data = json.loads(dd)
#         for i in data:
#             instance = Visual_dash(topic = i['topic'], title= i['title'], intensity=i['intensity'], sector = i['sector'], 
#                               url = i['url'], insight = i['insight'], region = i['region'], 
#                               impact = i['impact'],added = i['added'], published = i['published'], country=i['country'], 
#                               relevance = i['relevance'], pestle = i['pestle'], source = i['source'], likelihood = i['likelihood'])    
#             instance.save()

#     return HttpResponse("Data inserted successfully")




def d_view(request):
    VO = Visual_dash.objects.all()
    d = {'vo' : VO}
    return render(request, 'd_view.html', d)



def visual_board(request):
    VO = Visual_dash.objects.all()
    d = {'vo' : VO}
    return render(request, "visual_board.html")


# Barcharts get started 

def barchart(request):
    return render(request, 'barchart.html')
