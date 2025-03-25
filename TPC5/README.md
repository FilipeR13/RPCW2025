# TPC5: Processamento e Conversão de Dados de Filmes
## 2025/03/25

## Autor:
- PG55969
- José Filipe Ribeiro Rodrigues

## Resumo

Este projeto consiste em um conjunto de scripts Python que processam dados de filmes e atores, filtrando e combinando informações de diferentes fontes para gerar um dataset final em formato JSON. Além disso, os dados são convertidos para o formato RDF/Turtle.

### Estrutura do Projeto

- **generate_dataset.py:** Script responsável por carregar, filtrar e combinar dados de filmes e atores.
    - `load_and_filter_movies()`: Carrega e filtra dados de filmes.
    - `process_akas()`: Processa dados de títulos alternativos e idiomas originais.
    - `process_people()`: Processa dados de pessoas envolvidas nos filmes.
    - `combine_data()`: Combina todos os dados processados em um único dataset JSON.

- **script.py:** Script responsável por converter o dataset JSON para o formato RDF/Turtle.
    - `populate_genres(generos)`: Popula os gêneros no formato RDF.
    - `populate_languages(languages)`: Popula os idiomas no formato RDF.
    - `populate_countries(countries)`: Popula os países no formato RDF.
    - `populate_people(people)`: Popula as pessoas no formato RDF.
    - `populate_movies(movies)`: Popula os filmes no formato RDF.
    - `populate(filmes, atores, generos, languages, countries)`: Combina todas as populações em um único texto RDF.

### Coleta e Processamento de Dados

O processo de coleta e processamento de dados envolve as seguintes etapas:

1. **Carregamento e Filtragem de Filmes**: Carrega dados de filmes e filtra os registros relevantes.
2. **Processamento de Títulos Alternativos**: Processa dados de títulos alternativos e idiomas originais.
3. **Processamento de Pessoas**: Processa dados de pessoas envolvidas nos filmes.
4. **Combinação de Dados**: Combina todos os dados processados em um único dataset JSON.
5. **Conversão para RDF/Turtle**: Converte o dataset JSON para o formato RDF/Turtle.

### Instruções de Uso

1. Execute o script `generate_dataset.py` para gerar o dataset JSON:
    ```
    python generate_dataset.py
    ```

2. Execute o script `script.py` para converter o dataset JSON para RDF/Turtle:
    ```
    python script.py
    ```

3. Os dados convertidos serão armazenados no arquivo `result.ttl`.

### Exemplo de Dados RDF/Turtle

- **Exemplo de Gênero**:
    ```turtle
    :Western rdf:type owl:NamedIndividual ,
              :Genero .
    ```

- **Exemplo de Filme**:
    ```turtle
    :tt0000001 rdf:type owl:NamedIndividual ,
                :Filme ;
        :temArgumento :Argumento_tt0000001 ;
        :temGenero :Western ;
        :temLingua :ja ;
        :temPaisOrigem :JP ;
        :data "1906" ;
        :duracao 1 .
    ```

- **Exemplo de Pessoa**:
    ```turtle
    :nm0000001 rdf:type owl:NamedIndividual ,
                :Pessoa ;
        :nome "Fred Astaire" ;
        :funcao "actor" ;
        :categoria "actor" .
    ```
- **Exemplo de Língua**:
    ```turtle
    :en rdf:type owl:NamedIndividual ,
          :Lingua .
    ```

- **Exemplo de País**:
    ```turtle
    :US rdf:type owl:NamedIndividual ,
          :Pais .
    ```