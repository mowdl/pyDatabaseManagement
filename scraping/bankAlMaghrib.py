import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def alMaghrib():
    myUrl = 'http://www.bkam.ma/Marches/Principaux-indicateurs/Marche-des-changes/Cours-de-change/Cours-de-reference'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")

    rs = rows[2:5]

    prices = [r.span.text for r in rs]

    return {
        "EURO": prices[0],
        "USD": prices[1],
        "CAD": prices[2]
    }





