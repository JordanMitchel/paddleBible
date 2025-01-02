import pandas as pd

# Convert geolocation data to CSV
dataframe = pd.read_csv("./Data/geolocation", delimiter="\t", engine='python')
dataframe.to_csv("./Data/biblicalLonLat.csv", encoding='utf-8', index=False)

# Convert delimited biblical data to CSV
dataframe = pd.read_csv("./Data/delimitedBiblicalData", delimiter="\t")
dataframe.to_csv("./Data/biblicalLonLat2.csv", encoding='utf-8', index=False)

# Format the generated CSV file by removing unwanted characters
with open("./Data/biblicalLonLat2.csv", "r", encoding='utf-8') as textFile:
    text = ''.join([line for line in textFile]) \
        .replace(">", "").replace("~", "").replace("?", "")

# Write the formatted text to a new file
with open("./Data/biblicalLonLat2_formatted.csv", "w") as outputFile:
    outputFile.writelines(text)
