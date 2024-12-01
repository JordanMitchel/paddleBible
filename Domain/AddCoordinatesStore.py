import json
import pandas as pd
from Domain.db import DB


def insert_coordinates_store(csv_path, coll_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    coll = DB[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))

    collist = DB.list_collection_names()
    if "LonLats" in collist:
        print("The collection exists.")
        coll.drop()
    coll.insert_many(payload)
    print(coll.count_documents({}))
    return coll.count_documents({})
