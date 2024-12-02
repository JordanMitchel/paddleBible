from pymongo import MongoClient
from Domain.db import DB


def update_lonlats():
    # where ever there is specific lon lats
    mycol = DB["LonLats"]

    mycol.update_many({},
                      [{'$set':
                            {"NIV Name": '$ESV Name',
                             "MSG Name": '$ESV Name',
                             "NKJ Name": '$ESV Name',
                             "NLT Name": '$ESV Name'}
                        }
                       ]
                      )


update_lonlats()
