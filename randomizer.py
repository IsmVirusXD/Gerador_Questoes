import get_problems
def randomizer(lista_indexes): #iniciante adhoc = [1,2]
    default_url = "https://www.beecrowd.com.br/judge/pt/problems/index/"
    import random
    import requests
    import bs4
    import re

    index = random.choice(lista_indexes)

    html_doc = requests.get(default_url + str(index))

    soup = bs4.BeautifulSoup(html_doc.text, "html.parser")
    texto = soup.find(id="table-info").contents[0]
    group = int(re.search(r"of ([0-9]+)", texto).group(1))

    page = random.randint(1, group)

    return get_problems.getProblems(index, page)
