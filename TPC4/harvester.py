import json,requests 

endpoint = "https://dbpedia.org/sparql"

def query_graphdb(sparql_query):
    headers = {'Accept': 'application/json'}
    
    response = requests.get(endpoint, headers=headers, params={'query': sparql_query})
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: HTTP {response.status_code} - {response.text}")
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        raise Exception(f"Failed to decode JSON: {e}. Response text: {response.text}")

dataset = {
    "atores": [],
    "filmes": []
}

atores_set = set()

def get_filmes():
    sparql_query = """
    select distinct ?id ?pais ?producer ?abs ?genero where { 
        ?id a dbo:Film .
        ?id dbo:abstract ?abs .
        ?id dbp:country ?pais .
        ?id dbo:producer/dbp:name ?producer .
        ?id dbo:genre ?genero .
        filter(lang(?producer)="en") .
        filter(lang(?pais)="en") .
        filter(lang(?abs)="en") .
    } LIMIT 100
    """

    films = query_graphdb(sparql_query)
    for f in films['results']['bindings']:
        id = f['id']['value']

        sparql_query = f"""
        select distinct ?ator where {{ 
	        <{id}> dbo:starring ?ator .
        }}
        """

        atores = query_graphdb(sparql_query)

        for a in atores['results']['bindings']:
            atores_set.add(a['ator']['value'])

        dataset["filmes"].append(
            {
                "id": f['id']['value'],
                "pais": f['pais']['value'],
                "realizador": f['producer']['value'],
                "abs": f['abs']['value'],
                "genero": f['genero']['value'],
                "atores": [a['ator']['value'] for a in atores['results']['bindings']]
            }
        )
    
def get_atores():
    for id in atores_set:
        sparql_query = f"""
        select distinct ?nome ?dataNasc ?origem where {{ 
            <{id}> dbp:name ?nome .
            <{id}> dbp:birthDate ?dataNasc .
            <{id}> dbp:birthPlace ?origem .
        }}
        """

        ator = query_graphdb(sparql_query)

        for a in ator['results']['bindings']:
            dataset["atores"].append(
                {
                    "id": id,
                    "nome": a['nome']['value'],
                    "dataNasc": a['dataNasc']['value'],
                    "origem": a['origem']['value']
                }
            )
       
if __name__ == "__main__":
    get_filmes()
    get_atores()

    json.dump(dataset, open('dataset.json', 'w'), indent=4)