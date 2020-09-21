from scraping.bankAlMaghrib import alMaghrib
from scraping.bankPopulaire import bankPopulaire
from scraping.bankAttijari import bankAttijari
from names import names
# from banks dicts to currencies dicts


def bToC():

    banks = {
        "Bank Al Maghrib (moyen)": alMaghrib(),
        "Banque Populaire": bankPopulaire(),
        "Attijariwafa bank": bankAttijari()
    }

    curs = names.keys()

    prices1 = {}
    prices2 = {}

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

    for [prices, priceType] in [[prices1, 'billet'], [prices2, 'virement']]:

        for cur in curs:

            prices[cur] = {
                'sell': {},
                'buy': {}
            }

            for key in banks:

                if priceType in banks[key]:
                    prices[cur] = {
                        'sell': {**prices[cur]['sell'], **{key: banks[key][priceType][cur]['sell']}},
                        'buy': {**prices[cur]['buy'], **{key: banks[key][priceType][cur]['buy']}}
                    }

    return {
        'billet': prices1,
        'virement': prices2
    }


# print(bToC())
