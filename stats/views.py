import json

from django.views.generic.base import TemplateView, View
from django.http.response import HttpResponse
from stats.models import Stat


class HomeView(TemplateView):
    template_name = "index.html"


class AjaxDataView(View):
    def get(self, request):
        data = [['Date / Time', 'Up', 'Down']]
        for s in Stat.objects.all().order_by('date'):
            data.append([s.date.strftime("%Y-%m-%d %H:%M"), s.up, s.down])
        return HttpResponse(json.dumps(data))
