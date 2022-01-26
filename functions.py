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


def getDados() -> []:
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


def getProblems(index: int, page: int) -> list:
    '''
    Return the Code, Name and the Dificult
    '''
    from bs4 import BeautifulSoup
    import requests

    html_doc = requests.get(
        f"https://www.beecrowd.com.br/judge/pt/problems/index/{index}?page={page}")
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    lst = []
    data: str

    for values in soup.tbody.findAll('td'):
        # ID
        if values['class'] == ['id']:
            data = ''
            data = values.a.text + '|'

        # Name
        if values['class'] == ['large']:
            data = data + values.a.text + '|' + values.a['href'] + '|'

        # Dificult
        if values['class'] == ['tiny'] and values.text.isnumeric():
            data = data + values.text
            v = data.split('|')
            lst.append(v)

    return lst


def setCofig() -> []:
    dados = getDados()
    lista = []

    if dados[1]:
        lista.append(stng.check01.text())
    if dados[2]:
        lista.append(stng.check02.text())
    if dados[3]:
        lista.append(stng.check03.text())
    if dados[4]:
        lista.append(stng.check04.text())
    if dados[5]:
        lista.append(stng.check05.text())
    if dados[6]:
        lista.append(stng.check06.text())
    if dados[7]:
        lista.append(stng.check07.text())
    if dados[8]:
        lista.append(stng.check08.text())
    if dados[9]:
        lista.append(stng.check09.text())

    print(lista)

    return lista
