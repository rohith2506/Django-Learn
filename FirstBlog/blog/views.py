# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
import datetime


def hello(request):
	return HttpResponse("Hello World")

def current_time(request):
	now = datetime.datetime.now()
	return render(request,'cur_date.html',{'current_date':now})

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request,'later_date.html',{'offset':offset,'date':dt})
	return HttpResponse(html)

def meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
