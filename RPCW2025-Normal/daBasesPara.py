from rdflib import Namespace, Literal, URIRef, XSD, OWL, Graph, RDF, RDFS

EX = Namespace("http://www.semanticweb.org/josérodrigues/ontologies/2025/academia/")
g = Graph()
g.parse("sapientia_ind_estudaCom.ttl", format="ttl")

g.add((EX.daBasesPara, RDF.type, OWL.ObjectProperty))
g.add((EX.daBasesPara, RDFS.domain, EX.Disciplina))
g.add((EX.daBasesPara, RDFS.range, EX.Aplicação))

query = """
CONSTRUCT {
  ?disciplina :daBasesPara ?aplicacao .
}
WHERE {
  ?disciplina :éEstudadoEm ?conceito .
  ?conceito :temAplicaçãoEm ?aplicacao .
}
"""

result = g.query(query)

insert_query = """
INSERT {
  ?disciplina :daBasesPara ?aplicacao .
}
WHERE {
  ?disciplina :éEstudadoEm ?conceito .
  ?conceito :temAplicaçãoEm ?aplicacao .
}
"""

g.update(insert_query)

g.serialize(destination="sapientia_ind_daBasesPara.ttl", format="ttl")