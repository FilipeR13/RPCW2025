# TPC2: Resolução de queries sobre a história de Portugal usando SPARQL
## 2025/02/16

## Autor:
- PG55969
- José Filipe Ribeiro Rodrigues

## Resumo

O trabalho consiste na resolução de queries sobre a história de Portugal usando SPARQL. O objetivo é explorar um conjunto de dados RDF que descreve eventos históricos de Portugal e responder a várias perguntas sobre esses eventos.


## Resolução
## Query 1 - Quantidade de classes listadas

```
select ?class where {
    ?class a owl:Class .
}
```
## Query 2 - Listar todas as propriedades usadas pelos sujeitos da classe :Rei :

```
select distinct ?prop where {
    ?s a :Rei .
    ?s ?prop ?o .
}
```

## Query 3 - Quantos reis aparecem na ontologia?

``` 
select ?s where {
    ?s rdf:type :Rei .
} 
```
## Query 4 - Calcula uma tabela com o seu nome, data de nascimento e cognome.
```
select ?s ?nome ?dataNascimento ?cognome where {
    ?s rdf:type :Rei .
    ?s :nome ?nome .
    ?s :nascimento ?dataNascimento .
    ?s :cognomes ?cognome .
} 
```

## Query 5 - Acrescenta à tabela anterior a dinastia em que cada rei reinou.
```
select ?s ?nome ?dataNascimento ?cognome ?nomeDinastia where {
    ?s rdf:type :Rei .
    ?s :nome ?nome .
    ?s :nascimento ?dataNascimento .
    ?s :cognomes ?cognome .
    ?s :temReinado ?reinado .
    ?reinado :dinastia ?dinastia .
    ?dinastia :nome ?nomeDinastia . 
} 
```
## Query 6 - Qual a distribuição de reis pelas 4 dinastias?
```
select ?nomeDinastia (COUNT(?rei) AS ?quantidadeReis) where {
  ?rei rdf:type :Rei .
  ?rei :temReinado ?reinado .
  ?reinado :dinastia ?nomeDinastia .
}
GROUP BY ?nomeDinastia
```
## Query 7 - Lista os descobrimentos (sua descrição) por ordem cronológica.
```
select ?s ?des ?da where {
	?s rdf:type :Descobrimento .
	?s :notas ?des .
    ?s :data ?da .
}
ORDER BY ?da
```
## Query 8 - Lista as várias conquistas, nome e data, com o nome do rei que reinava no momento.

```
select ?s ?n ?d ?r where {
    ?s rdf:type :Conquista .
    ?s :nome ?n .
    ?s :data ?d .
    ?s :temReinado ?reinado .
    ?reinado :temMonarca ?rei .
    ?rei :nome ?r .
}
```
## Query 9 - Calcula uma tabela com o nome, data de nascimento e número de mandatos de todos os presidentes portugueses.
```
select ?nome ?data (COUNT(?mandato) AS ?numMandato) where{
	?s rdf:type :Presidente .
    ?s :nome ?nome .
	?s :nascimento ?data .
    ?s :mandato ?mandato .
} GROUP BY ?nome ?data
```
## Query 10 - Quantos mandatos teve o presidente Sidónio Pais? Em que datas iniciaram e terminaram esses mandatos?
```
select (COUNT(?mandato) AS ?numMandatos) ?inicio ?fim where{
	?s rdf:type :Presidente .
    ?s :nome "Sidónio Bernardino Cardoso da Silva Pais" .
    ?s :mandato ?mandato .
    ?mandato :comeco ?inicio .
    ?mandato :fim ?fim .
}  GROUP BY ?inicio ?fim
```
## Query 11 - Quais os nomes dos partidos politicos presentes na ontologia?
```
select ?nome where{
	?s rdf:type :Partido .
    ?s :nome ?nome .
}
```
## Query 12 - Qual a distribuição dos militantes por cada partido politico?
```
select ?nome (COUNT(?militante) AS ?NMilitante )where{
	?s rdf:type :Partido .
    ?s :nome ?nome .
	?s :temMilitante ?militante
} GROUP BY ?nome
```
## Query 13 - Qual o partido com maior número de presidentes militantes?

```
select ?nome (COUNT(?militante) AS ?NMilitante )where{
	?s rdf:type :Partido .
    ?s :nome ?nome .
	?s :temMilitante ?militante
} 
GROUP BY ?nome
ORDER BY DESC(?NMilitante)
LIMIT 1
```