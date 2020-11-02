from requests import get
from bs4 import BeautifulSoup as soup

from datetime import datetime
from dateutil.relativedelta import relativedelta

def bankPopulaire():

    # yesterday as dd/mm/yyyy
    yesterday = datetime.now() + relativedelta(days=-14)
    StringDate = yesterday.strftime('%d') + '/' + yesterday.strftime('%m') + '/' + yesterday.strftime('%Y')

    myUrl = 'https://bpnet.gbp.ma/Public/FinaServices/ExchangeRate'

    # params for the virement html requst
    params = {
        'Param.Type': 'vir',
        'Param.StringDate': StringDate,
        'Param.Label': ''
    }

    page_html1 = get(myUrl).text
    page_html2 = get(myUrl, params= params).text

    prices1 = {}
    prices2 = {}

    # curs to search for, {'name in site': 'name in app'}
    curs = {
        'USD': '$',
        'EUR': '€',
        'CAD': 'CAD',
        'GBP': '₤',
        'SAR': 'SAR',
        'CHF': 'CHF'
    }

    for page_html, prices in [[page_html1, prices1], [page_html2, prices2]]:
        psoup = soup(page_html, "html.parser")

        rows = psoup.findAll("tr")

        for row in rows[2:12]:

            tds = row.findAll("td")

            for key in curs:
                if key in tds[0].text:
                    prices[curs[key]] = {
                        'buy': tds[1].text.replace(",", "."),
                        'sell': tds[5].text.replace(",", ".")
                        }

    print('****** Banque Populaire done')
    return {
        'billet': prices1,
        'virement': prices2,
    }

