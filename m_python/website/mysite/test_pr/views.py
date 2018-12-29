from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.now()
    html = '<html><head></head><body><h1> %s </h2><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    list = [{'id': 1, 'name': '张贵山'}, {'id': 2, 'name': '王娅'}]
    return render_to_response('student.html', {'students': list})