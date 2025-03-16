# TPC4: Harvesting dados da DBpedia com SPARQL
## 2025/03/15

## Autor:
- PG55969
- José Filipe Ribeiro Rodrigues

## Resumo

Este projeto consiste em um script Python que coleta dados de filmes e atores da DBpedia utilizando consultas SPARQL. Os dados coletados são armazenados em um arquivo JSON para posterior análise.

### Estrutura do Projeto

- **harvester.py:** Contém funções para buscar dados de filmes e atores da DBpedia.
    - `query_graphdb(sparql_query)`: Executa uma consulta SPARQL e retorna os resultados em formato JSON.
    - `get_filmes()`: Busca dados de filmes da DBpedia e armazena-os no dataset.
    - `get_atores()`: Busca dados de atores da DBpedia e armazena-os no dataset.

### Coleta de Dados

O processo de coleta de dados envolve as seguintes etapas:

1. **Execução da Consulta SPARQL**: Cada função de coleta de dados executa uma consulta SPARQL específica para obter os dados necessários.
2. **Processamento dos Resultados**: Os resultados das consultas são processados e armazenados em um dataset.
3. **Armazenamento em JSON**: O dataset é salvo em um arquivo JSON para posterior análise.

### Exemplos de Consultas SPARQL

- **Consulta de Filmes**:
    ```sparql
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
    ```

- **Consulta de Atores**:
    ```sparql
    select distinct ?nome ?dataNasc ?origem where { 
        <{id}> dbp:name ?nome .
        <{id}> dbp:birthDate ?dataNasc .
        <{id}> dbp:birthPlace ?origem .
    }
    ```

## Instruções de Uso

1. Execute o script Python:
     ```
     python harvester.py
     ```

2. Os dados coletados serão armazenados no arquivo `dataset.json`.
