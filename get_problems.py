def getProblems(index, page):
    import bs4
    import requests

    html_doc = requests.get(f"https://www.beecrowd.com.br/judge/pt/problems/index/{index}?page={page}")
    soup = bs4.BeautifulSoup(html_doc.text, 'html.parser')

    links = []
    for text in soup.tbody.findAll('td'):
        if text['class'] == ["large"]:
            a_tag = text.a
            print(f"Name = {a_tag.contents[0]} \nLink = {a_tag['href']}\n\n")
            links.append(a_tag['href'])
    return a_tag


#print(soup.tbody.findAll('a'))
#print(soup.tbody)
#getProblems(1,1)