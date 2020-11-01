from scraping.bankAlMaghrib import alMaghrib
from scraping.bankAttijari import bankAttijari
from scraping.bankPopulaire import bankPopulaire
import json


for d in [alMaghrib(), bankAttijari(), bankPopulaire()]:
    print(json.dumps(d, indent=4))