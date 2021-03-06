from pymongo import MongoClient

class WeberDB(object):
    def __init__(self):
        client = MongoClient()
        self.db = client['weber']
    
    def collection_names(self):
        return self.db.collection_names()

    def find_document(self, collection, field, value):
        criteria = {'object.'+field: value}
        attrs = self.db[collection].find_one(criteria)
        return attrs