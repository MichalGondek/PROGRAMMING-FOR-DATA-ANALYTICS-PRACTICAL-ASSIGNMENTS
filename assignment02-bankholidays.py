# Assignment02  
# Bank Holidays 
# Author: Michal Gondek

import json

# Load JSON data from UK bank holidays
with open("bankholidays.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Pull holiday names and dates
ni = data['northern-ireland']['events']
englandwales = data['england-and-wales']['events']
scotland = data['scotland']['events']

print('Bank Holidays in Northern Ireland')
for h in ni:
     print(f"{h['title']}: {h['date']}")

ew_titles = {h["title"] for h in englandwales}
scot_titles = {h["title"] for h in scotland}

# Print those only in Northern Ireland 
print("\nHolidays unique to Northern Ireland:")
for h in ni:
    if h["title"] not in ew_titles and h["title"] not in scot_titles:
        print(f"{h['title']}: {h['date']}")
        
