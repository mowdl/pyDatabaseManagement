import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def bankAttijari():
    myUrl = 'https://attijarinet.attijariwafa.com/particulier/public/coursdevise'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")


    prices = {}


    curs = {
        'USD': 'USD',
        'EUR': 'EUR',
        'CANADIEN': 'CAD',
        'STERLING': 'GBP',
        'SAOUDIEN': 'SAR',
        'SUISSE': 'CHF'
    }


    for row in rows[1:]:

        tds = row.findAll("td")

        for key in curs:
            if key in tds[2].span.text:
                prices[curs[key]] = {
                    'buy': tds[3].span.text.rstrip("\n").replace(".", ","),
                    'sell': tds[4].span.text.rstrip("\n").replace(".", ",")
                    }

    return prices


print(bankAttijari())