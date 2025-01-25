import pandas as pd

# Convert geolocation data to CSV
dataframe = pd.read_csv("./data/geolocation", delimiter="\t", engine='python')
dataframe.to_csv("./data/biblicalLonLat.csv", encoding='utf-8', index=False)

# Convert delimited biblical data to CSV
dataframe = pd.read_csv("./data/delimitedBiblicalData", delimiter="\t")
dataframe.to_csv("./data/biblicalLonLat2.csv", encoding='utf-8', index=False)

# Format the generated CSV file by removing unwanted characters
with open("./data/biblicalLonLat2.csv", "r", encoding='utf-8') as textFile:
    text = textFile.read().replace(">", "").replace("~", "").replace("?", "")


# Write the formatted text to a new file
with open("./data/biblicalLonLat2_formatted.csv", "w", encoding='utf-8') as outputFile:
    outputFile.writelines(text)
