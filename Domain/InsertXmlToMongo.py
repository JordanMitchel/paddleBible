import pymongo
import xml.etree.ElementTree as ET
from Domain.db import MONGO_CLIENT


mydb = MONGO_CLIENT["school"]
mycol = mydb["students"]
import os
var = os.listdir("./../Data")

tree = ET.parse('./../Data/student.xml')

stud = tree.findall('student')

for ep in stud:
    name = ep.find('name').text
    age = ep.find('age').text
    section = ep.find('section').text

    stu_dict = [
                {'name': name, 'age': age, 'section': section}
               ]

    x = mycol.insert(stu_dict)

for y in mycol.find():
  print(y)