
def getProblems(index: int, page: int) -> list:
    from bs4 import BeautifulSoup
    import requests

    html_doc = requests.get(
        f"https://www.beecrowd.com.br/judge/pt/problems/index/{index}?page={page}")
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    lst = []
    data: str

    for values in soup.tbody.findAll('td'):
        if values['class'] == ['id']:
            data = ''
            data = values.a.text + '|'

        if values['class'] == ['large']:
            data = data + values.a.text + '|' + values.a['href'] + '|'

        if values['class'] == ['tiny'] and values.text.isnumeric():
            data = data + values.text
            v = data.split('|')
            lst.append(v)
    return lst
