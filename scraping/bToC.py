from scraping.bankAlMaghrib import alMaghrib
from scraping.bankPopulaire import bankPopulaire
from scraping.bankAttijari import bankAttijari


# from banks dicts to currencies dicts


def bToC():

    banks = {
        "Bank Al Maghrib (moyen)": alMaghrib(),
        "Banque Populaire": bankPopulaire(),
        "Attijariwafa bank": bankAttijari()
    }

    curs = [
        'USD',
        'EURO',
        'CAD',
        'GBP'
    ]

    prices = {}

    # prices = {
    #     'cur1': {
    #         'sell': {
    #             'bank1': '00',
    #             'bank2': '00'
    #         },
    #         'buy': {
    #             'bank1': '00',
    #             'bank2': '00'
    #         }
    #     },
    #     'cur1': {
    #         'sell': {
    #             'bank1': '00',
    #             'bank2': '00'
    #         },
    #         'buy': {
    #             'bank1': '00',
    #             'bank2': '00'
    #         }
    #     },
    # }

    for cur in curs:

        prices[cur] = {
            'sell': {},
            'buy': {}
        }


        for key in banks:
            prices[cur] = {
            'sell': {**prices[cur]['sell'], **{key: banks[key][cur]['sell']}},
            'buy': {**prices[cur]['buy'], **{key: banks[key][cur]['buy']}}
        }





    return prices

print(bToC())


