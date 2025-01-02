from opencage.geocoder import OpenCageGeocode

key = '0c12b649ffd54558846bde5342c92be4'
geocoder = OpenCageGeocode(key)

query = u'Ur middle east'

# no need to URI encode query, module does that for you
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
