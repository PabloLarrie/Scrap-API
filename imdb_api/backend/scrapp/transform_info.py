import json

with open('ejson.json') as f:
   data = json.load(f)

new_data = []

for dicc in data:
    to_append = {}
    to_append["model"] = "peliculas.Pelicula"
    to_append["pk"] = data.index(dicc) + 1
    to_append["fields"] = {key: value for (key, value) in dicc.items()}
    to_append["fields"]["id"] = data.index(dicc) + 1
    
    new_data.append(to_append)
   
fjson = json.dumps(new_data)
with open('results.json', 'w') as f:
    json.dump(new_data, f, indent=4)
   



