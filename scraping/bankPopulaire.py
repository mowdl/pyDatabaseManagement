import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def bankPopulaire():
    myUrl = 'https://bpnet.gbp.ma/Public/FinaServices/ExchangeRate'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")

    rs = rows[2:5]

    prices = [r.findAll("td")[1].text for r in rs]

    return {
        "EURO": prices[0],
        "USD": prices[1],
        "CAD": prices[2]
    }


# print(bankPopulaire())