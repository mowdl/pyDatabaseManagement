import csv
import firebase_admin
import google.cloud
import datetime
from firebase_admin import credentials, firestore

from scraping.bToC import bToC


cred = credentials.Certificate("dh-exchange-firebase-adminsdk-p8n1o-53dbdf224f.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

collection_name = "testCol"


data = bToC()

print(data)

time = datetime.datetime.now().strftime('%x')

doc = {
    'date': time,
    'data': data
}


store.collection(collection_name).document('testDoc1').set(doc)

