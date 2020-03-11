import requests
import json

link ="https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"
r = requests.get(link)
print(r)
file_name = 'results.json'
o = open('results.json', "w")
data = r.json()
print(type(data))
data =json.dumps(data)
o.write(json.dumps(data, indent = 2))
o.close()
