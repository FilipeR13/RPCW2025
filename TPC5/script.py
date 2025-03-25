import json

def open_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def populate_genres(generos):
    text_geners = ""
    for genero in generos:
        text_geners += f"""
:{genero} rdf:type owl:NamedIndividual ,
            :Genero .
    """
    return text_geners

def populate_languages(languages):
    text_languages = ""
    for language in languages:
        text_languages += f"""
:{language} rdf:type owl:NamedIndividual ,
            :Lingua .
    """
    return text_languages

def populate_countries(countries):
    text_countries = ""
    for country in countries:
        text_countries += f"""
:{country} rdf:type owl:NamedIndividual ,
            :Pais .
    """
    return text_countries

def populate_people(people):
    text_people = ""
    for person in people:
        text_people += f"""
:{person} rdf:type owl:NamedIndividual ,
            :Pessoa ;
            :nome "{people[person]}" .
    """
    return text_people

def populate_movies(movies):
    text_movies = ""
    for movie in movies:
        id = movie["id"]
        genres = ",".join([f":{t}" for t in movie["genres"]])
        originalLanguage = movie["originalLanguage"]
        og = ""

        if originalLanguage:
            og = f":temLingua :{originalLanguage};"

        text_movies += f"""
:{id} rdf:type owl:NamedIndividual ,
                :Filme ;
        :temArgumento :Argumento_{id} ;
        :temGenero {genres} ;
        {og}
        :temPaisOrigem :{movie["originalCountry"]} ;
        :data "{int(movie["releaseYear"])}" ;  # Aqui garantimos que a data seja um inteiro
        :duracao {movie["duration"]} .
    """

        for person in movie["peopleInvolved"]:
            person_id = person["nconst"]
            text_movies += f"""
:{person_id} rdf:type owl:NamedIndividual ,
                        :Pessoa ;
            :nome "{person["name"]}" ;
            :funcao "{person["job"]}" ;
            :categoria "{person["category"]}" .
    """
    return text_movies

def populate(filmes, atores, generos, languages, countries):
    result = populate_genres(generos)
    result += populate_languages(languages)
    result += populate_countries(countries)
    result += populate_people(atores)
    result += populate_movies(filmes)
    return result

if __name__ == '__main__':
    data = open_json('dataset.json')
    filmes = data['movies']
    atores = data['allPeople']
    generos = data['allGenres']
    languages = data['allLanguages']
    countries = data['allCountries']

    result = populate(filmes, atores, generos, languages, countries)

    with open('result.ttl', 'w') as f:
        f.write(result)