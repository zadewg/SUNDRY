
from urllib import urlopen
from lxml import etree
import requests, time
from bs4 import BeautifulSoup
import sys

words = []

def _getKeywords(url):
	global words
	html = urlopen(url).read()

	tree = etree.HTML(html)

	MM = tree.xpath("//meta[@name='Keywords']")
	if MM > 0:
		for i in MM:
			full = etree.tostring(i)
			full = full.replace('" />&#13;', "").replace('<meta name="keywords" content="', '').replace(',', '')
			for i in full.split():
				words.append(i)
		
	NN = tree.xpath("//meta[@name='keywords']")
	if NN > 0:
		for i in NN:
			full = etree.tostring(i)
			full = full.replace('" />&#13;', "").replace('<meta name="keywords" content="', '').replace(',', '')
			for i in full.split():
				words.append(i)
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
 
 
def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')
 
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
 
    return search_term, response.text
	
def parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
 
        link = result.find('a', href=True)
        if link:
            link = link['href']
            found_results.append(link)
            rank += 1
    return found_results

def scrape_google(search_term, number_results, language_code):
    try:
        keyword, html = fetch_results(search_term, number_results, language_code)
        results = parse_results(html, keyword) #OJO AQUI
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")


if __name__ == '__main__':
    #basewords = ['keywords', 'python', 'google scraping']
    basewords = ['partido popular']
    data = []
    for baseword in basewords:
        try:
            results = scrape_google(baseword, 20, "es")
            for result in results:
                data.append(result)
        except Exception as e:
            print(e)

    for i in data:
	try:
		#print(i)
		_getKeywords(i)
	except Exception as e:
		#print(e)
		pass
    print(words)







