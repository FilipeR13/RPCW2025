from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, XSD
import json

EX = Namespace("http://www.semanticweb.org/josérodrigues/ontologies/2025/academia/")

new_graph = Graph()
new_graph.parse("sapientia_base.ttl", format="turtle")

disciplinas = set()
conceitos_set = set()
periodo_historico = set()
aplicacoes = set()
conhecimentos = set()
mestres = set()

with open("data/conceitos.json", "r") as file:
    conceitos = json.load(file)["conceitos"]
    for conceito in conceitos:
        conceito_uri = EX[conceito["nome"].replace(" ", "_")]
        if conceito_uri not in conceitos_set:
            new_graph.add((conceito_uri, RDF.type, EX.Conceito))
            conceitos_set.add(conceito_uri)
        new_graph.add((conceito_uri, EX.nome, Literal(conceito["nome"], datatype=XSD.string)))
        for aplicacao in conceito["aplicações"]:
            aplicacao_uri = EX[aplicacao.replace(" ", "_")]
            if aplicacao_uri not in aplicacoes:
                new_graph.add((aplicacao_uri, RDF.type, EX.Aplicação))
                new_graph.add((aplicacao_uri, EX.nome, Literal(aplicacao, datatype=XSD.string)))
                aplicacoes.add(aplicacao_uri)
            new_graph.add((conceito_uri, EX.temAplicaçãoEm, aplicacao_uri))
        periodo = conceito["períodoHistórico"]
        periodo_uri = EX[periodo.replace(" ", "_")]
        if periodo_uri not in periodo_historico:
            new_graph.add((periodo_uri, RDF.type, EX.PeríodoHistorico))
            new_graph.add((periodo_uri, EX.nome, Literal(periodo, datatype=XSD.string)))
            periodo_historico.add(periodo_uri)
        new_graph.add((conceito_uri, EX.surgeEm, periodo_uri))

        for conceitos_relacionado in conceito["conceitosRelacionados"]:
            conceito_relacionado_uri = EX[conceitos_relacionado.replace(" ", "_")]
            if conceito_relacionado_uri not in conceitos_set:
                new_graph.add((conceito_relacionado_uri, RDF.type, EX.Conceito))
                conceitos_set.add(conceito_relacionado_uri)
            new_graph.add((conceito_uri, EX.temConceitoRelacionado, conceito_relacionado_uri))

with open("data/disciplinas.json", "r") as file:
    disciplinas_data = json.load(file)["disciplinas"]
    for disciplina in disciplinas_data:
        disciplina_uri = EX[disciplina["nome"].replace(" ", "_")]
        if disciplina_uri not in disciplinas:
            new_graph.add((disciplina_uri, RDF.type, EX.DIsciplina))
            disciplinas.add(disciplina_uri)
        new_graph.add((disciplina_uri, EX.nome, Literal(disciplina["nome"], datatype=XSD.string)))
        for conhecimento in disciplina["tiposDeConhecimento"]:
            conhecimento_uri = EX[conhecimento.replace(" ", "_")]
            if conhecimento_uri not in conhecimentos:
                new_graph.add((conhecimento_uri, RDF.type, EX.TipodeConhecimento))
                new_graph.add((conhecimento_uri, EX.nome, Literal(conhecimento, datatype=XSD.string)))
                conhecimentos.add(conhecimento_uri)
            new_graph.add((disciplina_uri, EX.pertenceA, conhecimento_uri))

        if "conceitos" in disciplina:
            for conceito in disciplina["conceitos"]:
                conceito_uri = EX[conceito.replace(" ", "_")]
                if conceito_uri not in conceitos_set:
                    new_graph.add((conceito_uri, RDF.type, EX.Conceito))
                    conceitos_set.add(conceito_uri)
                new_graph.add((conceito_uri, EX.éEstudadoEm, disciplina_uri))

with open("data/mestres.json", "r") as file:
    mestres_data = json.load(file)["mestres"]
    for mestre in mestres_data:
        mestre_uri = EX[mestre["nome"].replace(" ", "_")]
        new_graph.add((mestre_uri, RDF.type, EX.Mestre))
        new_graph.add((mestre_uri, EX.nome, Literal(mestre["nome"], datatype=XSD.string)))
        mestres.add(mestre_uri)
        periodo_uri = EX[mestre["períodoHistórico"].replace(" ", "_")]
        if periodo_uri not in periodo_historico:
            new_graph.add((periodo_uri, RDF.type, EX.PeríodoHistorico))
            new_graph.add((periodo_uri, EX.nome, Literal(mestre["períodoHistórico"], datatype=XSD.string)))
            periodo_historico.add(periodo_uri)
        new_graph.add((mestre_uri, EX.mestreEm, periodo_uri))

        for disciplina in mestre["disciplinas"]:
            disciplina_uri = EX[disciplina.replace(" ", "_")]
            if disciplina_uri not in disciplinas:
                new_graph.add((disciplina_uri, RDF.type, EX.DIsciplina))
                disciplinas.add(disciplina_uri)
            new_graph.add((mestre_uri, EX.ensina, disciplina_uri))
with open("data/obras.json", "r") as file:
    obras_data = json.load(file)["obras"]
    for obra in obras_data:
        obra_uri = EX[obra["titulo"].replace(" ", "_")]
        new_graph.add((obra_uri, RDF.type, EX.Obra))
        autor_uri = EX[obra["autor"].replace(" ", "_")]
        if autor_uri not in mestres:
            new_graph.add((autor_uri, RDF.type, EX.Mestre))
            new_graph.add((autor_uri, EX.nome, Literal(obra["autor"], datatype=XSD.string)))
            mestres.add(autor_uri)
        new_graph.add((obra_uri, EX.título, Literal(obra["titulo"], datatype=XSD.string)))
        new_graph.add((obra_uri, EX.foiEscritoPor, autor_uri))

        for conceito in obra["conceitos"]:
            conceito_uri = EX[conceito.replace(" ", "_")]
            if conceito_uri not in conceitos_set:
                new_graph.add((conceito_uri, RDF.type, EX.Conceito))
                conceitos_set.add(conceito_uri)
            new_graph.add((obra_uri, EX.explica, conceito_uri))

"""
  {
    "nome": "Cássia Berrelhas",
    "idade": 59,
    "disciplinas": [
      "Física",
      "Sociologia",
      "Música",
      "Artes",
      "Línguas",
      "Biologia"
    ]
  },
"""

with open("data/pg55969.json", "r") as file:
    data = json.load(file)
    for i, aprendiz in enumerate(data):
        aprendiz_uri = EX[aprendiz["nome"].replace(" ", "_") + f"_{i}"]
        new_graph.add((aprendiz_uri, RDF.type, EX.Aprendiz))
        new_graph.add((aprendiz_uri, EX.nome, Literal(aprendiz["nome"], datatype=XSD.string)))
        new_graph.add((aprendiz_uri, EX.idade, Literal(aprendiz["idade"], datatype=XSD.integer)))
        for disciplina in aprendiz["disciplinas"]:
            disciplina_uri = EX[disciplina.replace(" ", "_")]
            if disciplina_uri not in disciplinas:
                new_graph.add((disciplina_uri, RDF.type, EX.DIsciplina))
                disciplinas.add(disciplina_uri)
            new_graph.add((aprendiz_uri, EX.aprende, disciplina_uri))
        
new_graph.serialize(destination="sapientia_ind.ttl", format="turtle")
