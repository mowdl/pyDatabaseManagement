from scraping.bankAlMaghrib import alMaghrib
from scraping.bankPopulaire import bankPopulaire
from scraping.bankAttijari import bankAttijari


# from banks dicts to currencies dicts


def bToC():
    alMaghribData = alMaghrib()
    bankPopulaireData = bankPopulaire()
    bankAttijariData = bankAttijari()

    USD = {
        # "name": "USD",
        "Bank Al Maghrib": alMaghribData["USD"],
        "Banque Populaire": bankPopulaireData["USD"],
        "Attijariwafa bank": bankAttijariData["USD"]
    }

    EURO = {
        # "name": "EURO",
        "Bank Al Maghrib": alMaghribData["EURO"],
        "Banque Populaire": bankPopulaireData["EURO"],
        "Attijariwafa bank": bankAttijariData["EURO"]
    }

    CAD = {
        # "name": "CAD",
        "Bank Al Maghrib": alMaghribData["CAD"],
        "Banque Populaire": bankPopulaireData["CAD"],
        "Attijariwafa bank": bankAttijariData["CAD"]
    }

    return {
        'USD': USD,
        'EURO': EURO,
        'CAD': CAD,
    }


