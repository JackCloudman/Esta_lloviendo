import json,requests
from datetime import datetime
class Parser():
    def __init__(self,url):
        self.url = url
    def parse(self):
        r = requests.get(self.url)
        if r.status_code != 200:
            return False
        res = r.text.split("\n")[:-1]
        data = {}
        for r in res:
            r = r.split(' ')
            lat,lon = r[0].split(",")
            ts = datetime.strptime("%s %s"%(r[2],r[3]),"%Y-%m-%d %H:%M:%S").timestamp()
            data[r[1]] = {"lat":lat,"lon":lon,"ts":ts,"intensidad":r[4],
                          "status":0 if r[7]=="ret" else 1 }
        return data
