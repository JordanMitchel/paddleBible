import pandas

dataframe = pandas.read_csv("./Data/geoloocation", delimiter="\t", engine='python')

dataframe.to_csv("./Data/biblicalLonLat.csv", encoding='utf-8', index=False)


dataframe = pandas.read_csv("./Data/delimitedBiblicalData", delimiter="\t")

dataframe.to_csv("./Data/biblicalLonLat2.csv", encoding='utf-8', index=False)


import csv

text = open("./Data/biblicalLonLat2.csv", "r")
text = ''.join([i for i in text]) \
    .replace(">", "").replace("~","").replace("?","")
x = open("./Data/biblicalLonLat2_formatted.csv", "w")
x.writelines(text)
x.close()