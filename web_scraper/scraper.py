import requests
import pprint
from bs4 import BeautifulSoup

#URL =' https://en.wikipedia.org/wiki/NASA'




def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(title="Wikipedia:Citation needed")
    return len(results)
  
print(get_citations_needed_count('https://en.wikipedia.org/wiki/NASA')) 

def get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(title="Wikipedia:Citation needed")
    result = results.find_all('p')
    for i in result:
        
print( get_citations_needed_report('https://en.wikipedia.org/wiki/NASA'))    