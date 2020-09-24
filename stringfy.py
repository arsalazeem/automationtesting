import json


def tojson(self):
    return json.dumps(self, default=lambda o: o.__dict__)