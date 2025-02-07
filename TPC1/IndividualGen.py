import sys, json

clubes = set()
atletas = []
modalidades = {}
exames = []


def read_json(filename):
    if not filename.endswith(".json"):
        print("Error: input file must be a JSON file")
        sys.exit(1)
    
    with open(filename, "r") as file:
        data = json.load(file)
        return data

def export_data(data):
    for item in data:
        #remove spaces from clubes
        item["clube"] = item["clube"].replace(" ", "")
        clubes.add(item["clube"])
        if item["modalidade"] not in modalidades:
            modalidades[item["modalidade"]] = set([item["clube"]])
        else:
            modalidades[item["modalidade"]].add(item["clube"])
        atleta = {
            "nome": item["nome"]["primeiro"] + " " + item["nome"]["último"],
            "clube": item["clube"],
            "modalidade": item["modalidade"],
            "exame": "Exame" + item["nome"]["primeiro"] + item["nome"]["último"],
            "idade": str(item["idade"]),
            "género": item["género"],
            "morada": item["morada"],
            "federado": item["federado"],
            "email": item["email"],
        }
        atletas.append(atleta)
        exame = {
            "nome": "Exame" + item["nome"]["primeiro"] + item["nome"]["último"],
            "data": item["dataEMD"] + "T00:00:00",
            "resultado": item["resultado"]
        }
        exames.append(exame)

def write_clubes_file(file):
    for clube in clubes:
        file.write(f":{clube} rdf:type owl:NamedIndividual ,\n                 :Clube .\n\n")

def write_modalidades_file(file):
    for modalidade in modalidades:
        file.write(f":{modalidade} rdf:type owl:NamedIndividual ,\n                  :Modalidade ;\n")
        file.write(f"         :temNome \"{modalidade}\" .\n\n")

        for clube in modalidades[modalidade]:
            file.write(f"[ rdf:type owl:NegativePropertyAssertion ;\n")
            file.write(f"  owl:sourceIndividual :{modalidade} ;\n")
            file.write(f"  owl:assertionProperty :temClube ;\n")
            file.write(f"  owl:targetIndividual :{clube}\n")
            file.write(f"] .\n\n")

def write_exames_file(file):
    for exame in exames:
        file.write(f":{exame['nome']} rdf:type owl:NamedIndividual ,\n")
        file.write(f"                 :Exame ;\n")
        file.write(f"              :temData \"{exame['data']}\"^^xsd:dateTime ;\n")
        file.write(f"              :temResultado \"{exame['resultado']}\"^^xsd:boolean .\n\n")

def write_atletas_file(file):
    for atleta in atletas:
        nome_sem_espaco = atleta['nome'].replace(" ", "")
        file.write(f":{nome_sem_espaco} rdf:type owl:NamedIndividual ,\n")
        file.write(f"                       :Atleta ;\n")
        file.write(f"              :temNome \"{atleta['nome']}\" ;\n")
        file.write(f"              :temIdade \"{atleta['idade']}\"^^xsd:int ;\n")
        file.write(f"              :temGénero \"{atleta['género']}\" ;\n")
        file.write(f"              :temMorada \"{atleta['morada']}\" ;\n")
        file.write(f"              :éFederado \"{atleta['federado']}\"^^xsd:boolean ;\n")
        file.write(f"              :temEmail \"{atleta['email']}\" .\n\n")

        # Clube
        file.write(f"[ rdf:type owl:NegativePropertyAssertion ;\n")
        file.write(f"  owl:sourceIndividual :{nome_sem_espaco} ;\n")
        file.write(f"  owl:assertionProperty :temClube ;\n")
        file.write(f"  owl:targetIndividual :{atleta['clube']}\n")
        file.write(f"] .\n\n")

        # Exame
        file.write(f"[ rdf:type owl:NegativePropertyAssertion ;\n")
        file.write(f"  owl:sourceIndividual :{nome_sem_espaco} ;\n")
        file.write(f"  owl:assertionProperty :fazExame ;\n")
        file.write(f"  owl:targetIndividual :{atleta['exame']}\n")
        file.write(f"] .\n\n")

        # Modalidade
        file.write(f"[ rdf:type owl:NegativePropertyAssertion ;\n")
        file.write(f"  owl:sourceIndividual :{nome_sem_espaco} ;\n")
        file.write(f"  owl:assertionProperty :praticaModalidade ;\n")
        file.write(f"  owl:targetIndividual :{atleta['modalidade']}\n")
        file.write(f"] .\n\n")


def append_individuals_file(ttl_file):
    with open(ttl_file, "a") as file:
        file.write("\n\n")
        write_clubes_file(file)
        file.write("\n\n")
        write_modalidades_file(file)
        file.write("\n\n")
        write_exames_file(file)
        file.write("\n\n")
        write_atletas_file(file)
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python IndividualGen.py <input_file> <ttl_file>")
        sys.exit(1)

    json_data = read_json(sys.argv[1])

    export_data(json_data)

    print(len(exames))

    append_individuals_file(sys.argv[2])