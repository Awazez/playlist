from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_link_homepage():
    url = "https://www.bbc.co.uk/programmes/b006wq4s/episodes/player"
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    start_url = "https://www.bbc.co.uk/sounds/play/"
    links = []
    links_without_none = []
    lst = []

    for link in soup.findAll('a'):
        links.append(link.get('href'))
    for i in links: 
        if i != None : 
            links_without_none.append(i) 
    
    sounds_url = [x for x in links_without_none if x.startswith(start_url)]
    print(sounds_url[0])

get_link_homepage()