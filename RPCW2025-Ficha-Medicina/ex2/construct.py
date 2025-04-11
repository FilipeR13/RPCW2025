from rdflib import Graph, Namespace, RDF, OWL, RDFS, Literal, XSD

g = Graph()
g.parse("med_doentes.ttl")

n = Namespace("http://www.example.org/disease-ontology#")

q="""
CONSTRUCT {
    ?doente :hasDisease ?doenca .
}
WHERE {
    ?doente :hasSympton ?sintoma1, ?sintoma2, ?sintoma3 .
    ?doenca :hasSymptom ?sintoma1, ?sintoma2, ?sintoma3 .
    FILTER(?sintoma1 != ?sintoma2 && ?sintoma1 != ?sintoma3 && ?sintoma2 != ?sintoma3)
}
"""

for r in g.query(q):
    g.add(r)

g.serialize(destination="med_doentes_diagonisticados.ttl", format="turtle")