import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def bankAttijari():
    myUrl = 'https://attijarinet.attijariwafa.com/particulier/public/coursdevise'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")

    rs = rows[7:10]

    prices = [r.findAll("td", {"data-title": "Achat"})[0].text.rstrip("\n").replace(".", ",") for r in rs]


    return {
        "EURO": prices[1],
        "USD": prices[2],
        "CAD": prices[0]
    }

