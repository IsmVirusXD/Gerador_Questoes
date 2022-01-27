from distutils.core import run_setup
from random import Random
from typing import Union

from pkg_resources import ResolutionError
import settingspage as stng


def impDados():
    '''
    Print in the console each one of the Selected Filter (settingspage.py)
    '''
    print("Numeros de Questões: {}".format(stng.NQuest))

    print("01 - {}".format(stng.check01.get()))
    print("02 - {}".format(stng.check02.get()))
    print("03 - {}".format(stng.check03.get()))
    print("04 - {}".format(stng.check04.get()))
    print("05 - {}".format(stng.check05.get()))
    print("06 - {}".format(stng.check06.get()))
    print("07 - {}".format(stng.check07.get()))
    print("08 - {}".format(stng.check08.get()))
    print("09 - {}".format(stng.check09.get()))


def getDados() -> list:
    '''
    Return all the Configuration from the Filter (settingspage.py))
    '''
    dados = []
    dados.append(stng.NQuest.get())

    dados.append(stng.check01.get())
    dados.append(stng.check02.get())
    dados.append(stng.check03.get())

    dados.append(stng.check04.get())
    dados.append(stng.check05.get())
    dados.append(stng.check06.get())

    dados.append(stng.check07.get())
    dados.append(stng.check08.get())
    dados.append(stng.check09.get())

    return(dados)


def _getMaxProblems(themes: list) -> int:
    import bs4
    import requests

    html_doc = requests.get(f"https://www.beecrowd.com.br/judge/pt/categories")
    soup = bs4.BeautifulSoup(html_doc.text, 'html.parser')

    result = []
    for theme in themes:
        themeName = f"category-{theme}"
        result.append(
            int(soup.find("li", {"class": themeName}).find("b").text.split()[0]))
    return result


def getProblems(NQuestions: int, themes: list):
    rng = Random()
    maxNumProblems = _getMaxProblems(themes)
    result = []

    while len(result) < NQuestions:
        _theme = rng.randint(0, len(maxNumProblems)-1)
        value = rng.randint(0, maxNumProblems[_theme]-1)
        page  = (value//25)+1
        index = value%25
        theme = themes[_theme] #corrégi o curso
        result.append((theme, page, index))

    response = dict()
    for theme, page, index in result:
        if (theme, page) in response:
            response[(theme, page)].append(index)
        else:
            response[(theme, page)] = [index]

    result = []
    for key, indexes in response.items():
        theme, page = key
        result.append((theme, page, indexes))

    response = []
    for theme, page, indexes in result:
        for item in _getProblems(theme, page, indexes):
            response.append(item)

    return response


def _getProblems(theme: int, page: int, indexes: list) -> list:
    '''
    Return the Code, Name and the Dificult
    '''
    from bs4 import BeautifulSoup
    import requests

    html_doc = requests.get(
        f"https://www.beecrowd.com.br/judge/pt/problems/index/{theme}?page={page}")
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    lst = []

    values = list(soup.tbody.findAll('tr'))
    for i in indexes:
        value = values[i]
        dif = list(value.findAll("td", {"class": "tiny"}))[1].text

        data = [value.find("td", {"class": "id"}).a.text,
                value.find("td", {"class": "large"}).a.text,
                value.a['href'],
                dif]
        lst.append(data)

    return lst


def setCofig() -> list:
    dados = getDados()
    lista = []

    if dados[1]:
        lista.append(1)
    if dados[2]:
        lista.append(2)
    if dados[3]:
        lista.append(3)
    if dados[4]:
        lista.append(4)
    if dados[5]:
        lista.append(5)
    if dados[6]:
        lista.append(6)
    if dados[7]:
        lista.append(7)
    if dados[8]:
        lista.append(8)
    if dados[9]:
        lista.append(9)

    return lista
