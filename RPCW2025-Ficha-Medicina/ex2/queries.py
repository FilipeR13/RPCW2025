from rdflib import Graph, Namespace, RDF, OWL

g = Graph()
g.parse("med_doentes.ttl")

n = Namespace("http://www.example.org/disease-ontology#")

q="""
SELECT (COUNT(?doenca) AS ?n)
WHERE {
    ?doenca a :Disease .
}
"""

q2="""
SELECT ?doenca
WHERE {
    ?doenca a :Disease .
    ?doenca :hasSymptom :yellowish_skin .
}
"""

q3="""
SELECT ?doenca
WHERE {
    ?doenca a :Disease .
    ?doenca :hasTreatment :exercise .
}
"""

q4="""
SELECT ?name WHERE {
    ?doente a :Patient .
    ?doente :hasName ?name .
} ORDER BY ?name
"""

print("Total number of diseases:")
for r in g.query(q):
    print(r)

print("Diseases with yellowish skin symptom:")
for r in g.query(q2):
    print(r[0].split("#")[-1])

print("Total number of diseases with exercise treatment:")
for r in g.query(q3):
    print(r)

print("Patients' names:")
for r in g.query(q4):
    print(r[0].split("#")[-1])
