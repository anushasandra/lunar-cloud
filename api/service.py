from django.http import HttpResponse, StreamingHttpResponse
from django.conf.urls import patterns, include, url
from framework import WeberView
import json
from django.http.response import Http404
from weber.settings import weber_db
import time


class Service(WeberView):
    def get(self, *args, **kwargs):
        command = kwargs.get('command','all')
        responseText = ''
        
        if command=='all':
            pass
        elif command=='request':
            responseText = json.dumps({'request':dir(self.request)})
        elif command=='cookies':
            responseText = json.dumps({'cookies':self.request.COOKIES})
        elif command=='collections':
            responseText = json.dumps({'collections':weber_db.collection_names()})
        else:
            raise Http404('Command Not Found')
        return HttpResponse(responseText)

class Test(WeberView):
    def get(self, *args, **kwargs):
        def test(n):
            for i in range(int(n)):
                yield(str(i))
        return StreamingHttpResponse(test(kwargs.get('n',10)))

urlpatterns = patterns('',
url(r'^service/?(?P<command>[A-Za-z]*)$',Service.as_view,name='service'),
url(r'^service/test/?(?P<n>[0-9]*)$',Test.as_view, name='test'),
)
