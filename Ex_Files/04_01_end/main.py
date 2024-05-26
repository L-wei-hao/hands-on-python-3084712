import requests, json

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

last_twenty_years_list=[]

for x in last_twenty_years:
    last_twenty_years_list.append(last_twenty_years)

print(last_twenty_years_list)

with open('Ex_Files/04_01_end/last_20_years.CSV','w') as f:
    json.dump(last_twenty_years_list,f, indent = 2)



for year in last_twenty_years:
    
    if year['value'] == None:
        continue
    display_width = year["value"] // 10_000_000
    #print(f'{year["date"]}: {year["value"]}', "=" * display_width)
