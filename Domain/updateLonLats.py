from pymongo import MongoClient


def update_lonlats():
    # where ever there is specific lon lats
    client = MongoClient(host='localhost', port=27018, username="root", password="rootpassword")
    mydb = client["bibleData"]
    mycol = mydb["LonLats"]

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
