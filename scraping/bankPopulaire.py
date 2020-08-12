import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def bankPopulaire():
    myUrl = 'https://bpnet.gbp.ma/Public/FinaServices/ExchangeRate'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")


    prices = {}


    curs = {
        'USD': 'USD',
        'EUR': 'EUR',
        'CAD': 'CAD',
        'GBP': 'GBP',
        'SAR': 'SAR',
        'CHF': 'CHF'
    }


    for row in rows[2:12]:

        tds = row.findAll("td")

        for key in curs:
            if key in tds[0].text:
                prices[curs[key]] = {
                    'buy': tds[1].text,
                    'sell': tds[5].text
                    }


    return prices


print(bankPopulaire())