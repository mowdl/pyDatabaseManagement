import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def alMaghrib():
    myUrl = 'http://www.bkam.ma/Marches/Principaux-indicateurs/Marche-des-changes/Cours-de-change/Cours-de-reference'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")

    prices = {}


    curs = {
        'U.S.A': 'USD',
        'EURO': 'EURO',
        'CANADIEN': 'CAD',
        'LIVRE STERLING': 'GBP'
    }


    for row in rows[2:10]:

        tds = row.findAll("td")

        for key in curs:
            if key in tds[0].text:
                prices[curs[key]] = {
                    'buy': tds[1].text,
                    'sell': tds[1].text
                    }


    return prices

# print(alMaghrib())





