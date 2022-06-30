import requests

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=cafe&inputtype=textquery&locationbias=circle%3A10000000%40-23.55068%2C-46.63418&fields=name,place_id&key=[GoogleApiKey]"

payload= {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

import pandas as pd

df = pd.DataFrame(data=response["candidates"])

#writing to Excel

datatoexcel = pd.ExcelWriter('C:/xampp/htdocs/diretorio/ConsumindoAPIs/Relatorios/APIGooglePlaces.xlsx')

# write DataFrame to excel

df.to_excel(datatoexcel)

# save the excel

datatoexcel.save()

print('DataFrame is written to Excel File successfully.')
