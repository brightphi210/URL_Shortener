from django.shortcuts import render, redirect

from django.http import JsonResponse

import uuid

import json

from .models import UrlApp

# Create your views here.

def index(request):
    return render(request, 'index.html')


def url_get(request):

    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[0:5]
        fetch_input = json.loads(request.body)

        new_fetch_input = fetch_input['new_input_field']

        link = new_fetch_input

        url_data = UrlApp(link = link, uid = uid)

        url_data.save()

        print('UID' , uid)
        
    return JsonResponse(uid, safe=False)


def go(request, pk):
    out_put = UrlApp.objects.get(uid = pk)
    new_out_put = str(out_put.link)

    if new_out_put.startswith('https://'):
        new_out_put = (new_out_put.replace('https://', ''))
    return redirect('https://' + new_out_put)