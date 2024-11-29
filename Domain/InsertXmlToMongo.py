import pymongo
import xml.etree.ElementTree as ET

from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27018/")
client = MongoClient(host='localhost', port=27018, username="root", password="rootpassword")
mydb = client["school"]
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