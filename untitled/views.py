from django.http import *
from untitled.models import *
import templates
import json
from django.shortcuts import *
from untitled.forms import *
from django.template.context_processors import csrf

def home(request):
    c={}
    c.update(csrf(request))
    c['form'] = MyForm()
    return render(request, 'index.html', c)


def add(request):
    s = json.dumps(request.POST, skipkeys=True, allow_nan=True)
    m = MyModel.objects.create(data=s)
    m.save()
    return HttpResponse(m.data)