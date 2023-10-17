import json

data = json.load(open(r"../vtuberscraper/vtuberscraper/spiders/vtuberdata.json", encoding='utf8'))

with open('data.json', 'w') as f:
    f.write(json.dumps(data, indent=4))