# TPC1: Geração de indíviduos para um ficheiro .ttl
## 2025/02/09

## Autor:
- PG55969
- José Filipe Ribeiro Rodrigues

## Resumo

Este programa, desenvolvido em Python, gera indivíduos para um ficheiro .ttl a partir de um ficheiro JSON. Ele processa dados de atletas, clubes, modalidades e exames, e exporta essas informações em formato RDF.

## Resolução

O programa foi desenvolvido em Python e utiliza a biblioteca `json` para ler e processar os dados do ficheiro JSON.

### Leitura e Exportação de Dados

- **Leitura de JSON:** O programa lê um ficheiro JSON contendo informações sobre atletas, clubes, modalidades e exames.
- **Processamento de Dados:** Os dados são processados e organizados em estruturas de dados apropriadas (listas e dicionários) para facilitar a exportação.

### Escrita de Dados em Formato RDF

- **Clubes:** Gera indivíduos RDF para cada clube.
- **Modalidades:** Gera indivíduos RDF para cada modalidade e associa os clubes correspondentes.
- **Exames:** Gera indivíduos RDF para cada exame realizado pelos atletas.
- **Atletas:** Gera indivíduos RDF para cada atleta, incluindo informações pessoais, clube, modalidade e exame associado.

## Instruções de Uso

Execute o programa a partir do terminal, fornecendo o arquivo JSON e o arquivo .ttl como argumentos.

```
python IndividualGen.py datasets/emd.json exames.ttl
```
