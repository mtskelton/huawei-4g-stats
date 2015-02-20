import json
import re
import requests

from django.core.management.base import BaseCommand

from stats.models import Stat


class Command(BaseCommand):
    def _get_stat(self, wan_stats, key):
        if key in wan_stats:
            return int(wan_stats[key])
        return 0

    def handle(self, *args, **options):
        r = requests.get("http://192.168.1.1/html/status/waninforefresh.asp")
        if r.status_code == 200 and re.search("^WanStatistics", r.text):
            lines = r.text.splitlines()
            wan_stats = json.loads(re.sub("'", "\"",
                                          re.sub("^WanStatistics = |;$", "",
                                                 lines[0])))

            stat = Stat(down=self._get_stat(wan_stats, 'downvolume'),
                        up=self._get_stat(wan_stats, 'upvolume'),
                        live_time=self._get_stat(wan_stats, 'liveTime'))
            stat.save()
