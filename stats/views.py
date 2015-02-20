import json

from django.views.generic.base import TemplateView, View
from django.http.response import HttpResponse
from stats.models import Stat


class HomeView(TemplateView):
    template_name = "index.html"


class AjaxDataView(View):
    def get(self, request):
        show_up = request.GET.get('show_up', 'false') == 'true'
        show_down = request.GET.get('show_down', 'false') == 'true'

        row = ['Date / Time']
        if show_up:
            row.append('Up')
        if show_down:
            row.append('Down')
        data = [row]
        for s in Stat.objects.all().order_by('date'):
            row = [s.date.strftime("%Y-%m-%d %H:%M")]
            if show_up:
                row.append(s.up / 1024)
            if show_down:
                row.append(s.down / 1024)
            data.append(row)
        return HttpResponse(json.dumps(data))
