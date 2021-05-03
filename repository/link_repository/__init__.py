from firebase_admin import credentials, firestore, initialize_app
from flask import jsonify


class LinkRepository:
    def __init__(self):
        # cred = credentials.Certificate("key.json")
        # default_app = initialize_app(cred)
        # db = firestore.client()
        # self.link_ref = db.collection("link")
        pass

    def get_link(self, slug):
        try:
            # link = self.link_ref.document(slug).get()
            return "jsonify(link.to_dict())", 200
        except:
            return "An error has occurred"
