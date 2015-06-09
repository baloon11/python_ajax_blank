# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
import json

def home(request):
    return render_to_response('index.html',
                               context_instance=RequestContext(request))
def function_for_ajax (request):
    if request.method == "POST" and request.is_ajax():
        first_field_squared=float(request.POST.get("first_field", ""))**2
        return HttpResponse(json.dumps({"result":first_field_squared}),
                            content_type="application/json")

