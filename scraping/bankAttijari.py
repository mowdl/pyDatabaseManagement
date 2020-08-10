import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def bankAttijari():
    myUrl = 'https://attijarinet.attijariwafa.com/particulier/public/coursdevise'

    page_html = uReq(myUrl).read()

    psoup = soup(page_html, "html.parser")

    rows = psoup.findAll("tr")

    for row in rows[1:]:

        tds = row.findAll("td")

        if "USD" in tds[2].span.text:
            buyUSD = tds[3].span.text.rstrip("\n").replace(".", ",")

        if "EURO" in tds[2].span.text:
            buyEURO = tds[3].span.text.rstrip("\n").replace(".", ",")

        if "CANADIEN" in tds[2].span.text:
            buyCAD = tds[3].span.text.rstrip("\n").replace(".", ",")
        

    return {
        "EURO": buyEURO,
        "USD": buyUSD,
        "CAD": buyCAD
    }


print(bankAttijari())