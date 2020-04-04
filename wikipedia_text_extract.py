import requests
from bs4 import BeautifulSoup

def get_wikitext(page_title):
    """
    API: https://www.mediawiki.org/wiki/API:Parsing_wikitext
    Example Usage:
    print(get_wikitext('Nepal'))
    """
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": page_title,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    raw_html = DATA["parse"]["text"]["*"]
    soup = BeautifulSoup(raw_html)
    text = soup.get_text()
    
    return text
