import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/gun'
# get_citations_needed_count(url)


def get_citations_needed_count(url):
    soup=BeautifulSoup(requests.get(url).content,'html.parser')
    citations= soup.findAll(text='citation needed')
    return print(len(citations))


def get_citations_needed_report(url):
    soup=BeautifulSoup(requests.get(url).content,'html.parser')
    all_pargrapgh = soup.find_all('p')
    all_citations=[]
    for p in all_pargrapgh:
        citation = p.find('a', { "title" : "Wikipedia:Citation needed"})
        if citation:
            all_citations.append(p.text)
    return all_citations


print(get_citations_needed_report(url))