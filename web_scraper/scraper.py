import requests
import pprint
from bs4 import BeautifulSoup
import json


#URL =' https://en.wikipedia.org/wiki/NASA'




def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(title="Wikipedia:Citation needed")
    return len(results)
  
print(get_citations_needed_count('https://en.wikipedia.org/wiki/NASA')) 

def get_citations_needed_report(URL):
 
    page = requests.get(URL)
    all_results = BeautifulSoup(page.content, 'html.parser').find_all('p')
    result = ''
    for i in all_results:
        try:
            if i.find_all('a', title='Wikipedia:Citation needed'):
                for j in range(len(i.text)):
                    if i.text[j] == '[' and i.text[j+16] == ']':
                        dot_in = 0
                        for jj in range(len(i.text[:j-5])):
                            if i.text[:j][jj] == '.':
                                dot_in = jj+2
                        result += f'\n\nThis sentence need citation: {i.text[:j][dot_in:]}\nand the full article is:\n  {i.text}'
        except:
            continue
    return result



if __name__ == "__main__":
    #print(get_citations_needed_count("https://en.wikipedia.org/wiki/NASA"))
    print( get_citations_needed_report("https://en.wikipedia.org/wiki/NASA")) 
    
   