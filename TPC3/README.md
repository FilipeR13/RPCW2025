# TPC3: Quiz sobre a história de Portugal usando Flask
## 2025/03/01

## Autor:
- PG55969
- José Filipe Ribeiro Rodrigues

## Resumo

Este projeto consiste em um quiz sobre a história de Portugal, desenvolvido utilizando Flask para o backend e Jinja templates para o frontend. O quiz obtém perguntas de uma base de dados SPARQL e apresenta-as aos utilizadores, que podem responder e ver a sua pontuação.

## Resolução

O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:
- `Flask`: Para criar o servidor web e gerenciar as rotas.
- `Jinja`: Para renderizar os templates HTML.
- `SPARQLWrapper`: Para executar consultas SPARQL na base de dados.

### Estrutura do Projeto

- **fetch_questions.py:** Contém funções para buscar perguntas da base de dados SPARQL.
    - `execute_query(query)`: Executa uma consulta SPARQL e retorna os resultados.
    - `fetch_questions_from_dbpedia()`: Busca várias perguntas da base de dados e retorna uma lista de perguntas.
    - Funções específicas para buscar diferentes tipos de perguntas, como `fetch_question_birth()`, `fetch_question_dinasty()`, etc.

- **app_hportugal.py:** Configura o servidor Flask e define as rotas para o quiz.
    - Rota `/`: Inicializa a sessão do utilizador e redireciona para a rota `/quiz`.
    - Rota `/quiz`: Apresenta uma pergunta ao utilizador e processa a resposta.
    - Rota `/score`: Exibe a pontuação final do utilizador.

### Geração de Perguntas

As perguntas são geradas dinamicamente a partir de consultas SPARQL à base de dados. O processo de geração de perguntas envolve as seguintes etapas:

1. **Execução da Consulta SPARQL**: Cada função de geração de perguntas executa uma consulta SPARQL específica para obter os dados necessários.
2. **Seleção Aleatória**: A partir dos resultados da consulta, uma entrada é selecionada aleatoriamente para formar a base da pergunta.
3. **Formatação da Pergunta**: A pergunta é formatada em texto, e as opções de resposta são geradas. Dependendo do tipo de pergunta, as opções podem ser respostas corretas ou alternativas incorretas geradas aleatoriamente.
4. **Embaralhamento das Opções**: As opções de resposta são embaralhadas para garantir que a resposta correta não esteja sempre na mesma posição.

### Tipos de Perguntas

O quiz inclui dois tipos principais de perguntas:

1. **Escolha Múltipla**: O utilizador deve escolher a resposta correta entre quatro opções. Exemplos incluem:
    - Data de nascimento de um rei ou presidente.
    - Dinastia de um rei.

2. **Verdadeiro ou Falso**: O utilizador deve determinar se uma afirmação é verdadeira ou falsa. Exemplos incluem:
    - Número de reis em uma dinastia.
    - Cognome de um rei.

### Exemplos de Perguntas

- **Escolha Múltipla**:
    - "What is the date of birth of King Afonso I?"
    - "What is the dinasty of King John I?"

- **Verdadeiro ou Falso**:
    - "The dinasty Avis had 7 kings. True or False?"
    - "The cognome of King Manuel I is 'The Fortunate'. True or False?"

## Instruções de Uso

1. Instale as dependências necessárias:
     ```
     pip install Flask SPARQLWrapper flask-cors
     ```

2. Execute o servidor Flask:
     ```
     python app_hportugal.py
     ```

3. Acesse o quiz no navegador através do endereço:
     ```
     http://localhost:5000
     ```
