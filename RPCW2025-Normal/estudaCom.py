from rdflib import Namespace, Literal, URIRef, XSD, OWL, Graph, RDF, RDFS

EX = Namespace("http://www.semanticweb.org/josérodrigues/ontologies/2025/academia/")
g = Graph()
g.parse("sapientia_ind.ttl", format="ttl")

g.add((EX.estudaCom, RDF.type, OWL.ObjectProperty))
g.add((EX.estudaCom, RDFS.domain, EX.Aprendiz))
g.add((EX.estudaCom, RDFS.range, EX.Mestre))

query = """
CONSTRUCT {
  ?aprendiz :estudaCom ?mestre .
}
WHERE {
  ?aprendiz :aprende ?disciplina .
  ?mestre :ensina ?disciplina .
}
"""

result = g.query(query)

print(len(result))

insert_query = """
INSERT {
  ?aprendiz :estudaCom ?mestre .
}
WHERE {
  ?aprendiz :aprende ?disciplina .
  ?mestre :ensina ?disciplina .
}
"""

g.update(insert_query)


g.serialize(destination="sapientia_ind_estudaCom.ttl", format="ttl")