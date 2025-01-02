from opencage.geocoder import OpenCageGeocode

KEY = '0c12b649ffd54558846bde5342c92be4'
geocoder = OpenCageGeocode(KEY)

QUERY = 'Ur middle east'

# no need to URI encode query, module does that for you
results = geocoder.geocode(QUERY)

print(f"{results[0]['geometry']['lat']},"
      f" {results[0]['geometry']['lng']},"
      f"{results[0]['components']['country_code']}"
      f"{results[0]['annotations']['timezone']['name']}")
