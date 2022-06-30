import requests

# exemple url google = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY"
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=cafe&inputtype=textquery&locationbias=circle%3A10000000%40-23.55068%2C-46.63418&fields=name,place_id&key=[GoogleApiKey]"

payload= {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

import pandas as pd

df = pd.DataFrame(data=response["results"])

#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/ConsumindoAPIs/Relatorios/APIGooglePlaces.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
