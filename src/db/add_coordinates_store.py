from io import StringIO

import aiofiles
import pandas as pd

from src.db.config import get_database

async def insert_coordinates_store(csv_path, coll_name):
    async with aiofiles.open(csv_path, 'r') as file:
        data = await file.read()
        csv_data = StringIO(data)
        df = pd.read_csv(csv_data)
        json_data = df.to_dict(orient='records')

        await insert_to_mongo(json_data,coll_name)


async def insert_to_mongo(data, coll_name):
    db =await  get_database()
    coll = db[coll_name]
    collist = await db.list_collection_names()

    if "LonLats" in collist:
        print("The collection exists.")
        await coll.drop()
    await coll.insert_many(data)
    count = await coll.count_documents({})
    print(count)
    return count
