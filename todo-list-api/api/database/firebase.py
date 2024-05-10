import firebase_admin
from firebase_admin import credentials
import pyrebase
import json
import os
from dotenv import load_dotenv

# loading environement variables
load_dotenv()
firebase_service_account_key = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")
firebase_config = os.getenv("FIREBASE_CONFIG")

# Initialisation  Firebase Admin
cred = credentials.Certificate(json.loads(firebase_service_account_key, strict=False))
firebase_admin.initialize_app(cred)

# Initialisation  Pyrebase
firebase = pyrebase.initialize_app(json.loads(firebase_config, strict=False))
db = firebase.database()
firebase_auth = firebase.auth()
