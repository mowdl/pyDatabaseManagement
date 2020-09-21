import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def bankAttijari():
    myUrl1 = 'https://attijarinet.attijariwafa.com/particulier/public/coursdevise'

    page_html1 = uReq(myUrl1).read()

    psoup1 = soup(page_html1, "html.parser")

    pDate = psoup1.findAll('div',{'class':'block-header'})[1].b.text.replace('-','/')

    myUrl2 = myUrl1 + '/search?dateCours='+ pDate +'&typeOperation=Virement'

    page_html2 = uReq(myUrl2).read()

    psoup2 = soup(page_html2, "html.parser")

    prices1 = {}
    prices2 = {}



    curs = {
        'USD': 'USD',
        'EUR': 'EUR',
        'CANADIEN': 'CAD',
        'STERLING': 'GBP',
        'SAOUDIEN': 'SAR',
        'SUISSE': 'CHF'
    }


    for [prices, psoup] in [[prices1, psoup1], [prices2, psoup2]]:

        rows = psoup.findAll("tr")

        for row in rows[1:]:

            tds = row.findAll("td")

            for key in curs:
                if key in tds[2].span.text:
                    prices[curs[key]] = {
                        'buy': tds[3].span.text.rstrip("\n").replace(".", ","),
                        'sell': tds[4].span.text.rstrip("\n").replace(".", ",")
                        }
    print('****** Attijariwafa done')	
    return {
        'billet': prices1,
        'virement': prices2,
    }


# print(bankAttijari())
