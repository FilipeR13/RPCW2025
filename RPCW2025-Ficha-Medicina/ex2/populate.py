from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, XSD
import csv, json

EX = Namespace("http://www.example.org/disease-ontology#")

existing_graph = Graph()
existing_graph.parse("medical.ttl", format="turtle")

new_graph = Graph()

new_graph.bind("", EX)
new_graph.bind("owl", OWL)
new_graph.bind("rdf", RDF)
new_graph.bind("rdfs", RDFS)

new_graph.add((EX.Ontology, RDF.type, OWL.Ontology))

new_graph.add((EX.Disease, RDF.type, OWL.Class))
new_graph.add((EX.Symptom, RDF.type, OWL.Class))
new_graph.add((EX.Treatment, RDF.type, OWL.Class))
new_graph.add((EX.Patient, RDF.type, OWL.Class))

new_graph.add((EX.hasSymptom, RDF.type, OWL.ObjectProperty))
new_graph.add((EX.hasSymptom, RDFS.domain, EX.Disease))
new_graph.add((EX.hasSymptom, RDFS.range, EX.Symptom))

new_graph.add((EX.hasTreatment, RDF.type, OWL.ObjectProperty))
new_graph.add((EX.hasTreatment, RDFS.domain, EX.Disease))
new_graph.add((EX.hasTreatment, RDFS.range, EX.Treatment))

new_graph.add((EX.Description, RDF.type, OWL.DatatypeProperty))
new_graph.add((EX.Description, RDFS.domain, EX.Disease))
new_graph.add((EX.Description, RDFS.range, XSD.string))

new_graph.add((EX.hasSympton, RDF.type, OWL.ObjectProperty))
new_graph.add((EX.hasSympton, RDFS.domain, EX.Patient))
new_graph.add((EX.hasSympton, RDFS.range, EX.Symptom))

new_graph.add((EX.hasName, RDF.type, OWL.DatatypeProperty))
new_graph.add((EX.hasName, RDFS.domain, EX.Patient))
new_graph.add((EX.hasName, RDFS.range, XSD.string))

new_graph.add((EX.Id, RDF.type, OWL.DatatypeProperty))
new_graph.add((EX.Id, RDFS.domain, EX.Patient))
new_graph.add((EX.Id, RDFS.range, XSD.integer))

with open("datasets/Disease_Syntoms.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    symptoms_set = set()

    for row in reader:
        disease = row["Disease"].strip().replace(" ", "_")
        disease_uri = EX[disease]
        new_graph.add((disease_uri, RDF.type, EX.Disease))

        symptoms = [
            row[f"Symptom_{i}"].strip().replace(" ", "_")
            for i in range(1, 18)
            if row[f"Symptom_{i}"]
        ]

        for symptom in symptoms:
            symptom_uri = EX[symptom]
            new_graph.add((symptom_uri, RDF.type, EX.Symptom))
            new_graph.add((disease_uri, EX.hasSymptom, symptom_uri))
            symptoms_set.add(symptom)

with open("datasets/Disease_Description.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        disease = row["Disease"].strip().replace(" ", "_")
        disease_uri = EX[disease]
        description = row["Description"].strip()
        new_graph.add((disease_uri, EX.Description, Literal(description)))


with open("datasets/Disease_Treatment.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        disease = row["Disease"].strip().replace(" ", "_")
        disease_uri = EX[disease]
        treatments = [
            row[f"Precaution_{i}"].strip().replace(" ", "_")
            for i in range(1, 5)
            if row[f"Precaution_{i}"]
        ]
        for treatment in treatments:
            treatment_uri = EX[treatment]
            new_graph.add((treatment_uri, RDF.type, EX.Treatment))
            new_graph.add((disease_uri, EX.hasTreatment, treatment_uri))

with open("datasets/doentes.json", "r") as json_file:
    i = 0
    data = json.load(json_file)
    for patient in data:
        name = patient["nome"].strip().replace(" ", "_")
        name_uri = EX[name]
        new_graph.add((name_uri, RDF.type, EX.Patient))
        new_graph.add((name_uri, EX.hasName, Literal(patient["nome"])))
        new_graph.add((name_uri, EX.Id, Literal(i)))
        i += 1
        for symptom in patient["sintomas"]:
            symptom_uri = EX[symptom.strip().replace(" ", "_")]
            new_graph.add((name_uri, EX.hasSympton, symptom_uri))

existing_graph += new_graph

existing_graph.serialize(destination="med_doentes.ttl", format="turtle")