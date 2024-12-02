import json
from io import StringIO

import aiofiles
import pandas as pd

from Domain.db import DB

async def insert_coordinates_store(csv_path, coll_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    async with aiofiles.open(csv_path, 'r') as file:
        data = await file.read()
        csv_data = StringIO(data)

        df = pd.read_csv(csv_data)
        json_data = df.to_dict(orient='records')

        await insert_to_mongo(json_data,coll_name)


async def insert_to_mongo(data, coll_name):
    coll = DB[coll_name]
    collist = await DB.list_collection_names()
    if "LonLats" in collist:
        print("The collection exists.")
        coll.drop()
    await coll.insert_many(data)
    count = await coll.count_documents({})
    print(count)
    return count
