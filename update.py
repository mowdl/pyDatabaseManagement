import csv
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

from scraping.bToC import bToC


cred = credentials.Certificate("dh-exchange-firebase-adminsdk-p8n1o-53dbdf224f.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

collection_name = "testCol"


store.collection(collection_name).document('testDoc').set(bToC())

