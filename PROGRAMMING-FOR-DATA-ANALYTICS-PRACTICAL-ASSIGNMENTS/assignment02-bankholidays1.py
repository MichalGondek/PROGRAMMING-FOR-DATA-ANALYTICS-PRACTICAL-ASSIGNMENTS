# Assignment02  
# Bank Holidays 
# Author: Michal Gondek

# Import data
import requests

# Import live UK bank holiday data
url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Extract holidays by region
ni = data["northern-ireland"]["events"]
england_wales = data["england-and-wales"]["events"]
scotland = data["scotland"]["events"]

# Print Northern Ireland holidays
print("Bank Holidays in Northern Ireland:\n")
for event in ni:
    print(f"{event['title']} on {event['date']}")

# Identify holidays unique to Northern Ireland
ew_titles = {h["title"] for h in england_wales}
scot_titles = {h["title"] for h in scotland}

unique_ni = [h for h in ni if h["title"] not in ew_titles and h["title"] not in scot_titles]

# Print unique holidays
print("\nHolidays unique to Northern Ireland:\n")
for event in unique_ni:
    print(f"{event['title']} on {event['date']}")
