from io import StringIO

import aiofiles
import pandas as pd
from domain.src.services.db_connector import insert_to_mongo


async def update_coordinates_collection_using_file(csv_path, coll_name):
    async with aiofiles.open(csv_path, 'r') as file:
        data = await file.read()
        csv_data = StringIO(data)
        df = pd.read_csv(csv_data)
        json_data = df.to_dict(orient='records')

        await insert_to_mongo(json_data, coll_name)



