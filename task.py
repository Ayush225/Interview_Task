import requests
from bs4 import BeautifulSoup

def get_settlement_details(date):
    url = f'https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/8381/FUT?strategy=DEFAULT&tradeDate={date}&pageSize=500'


    # Send an HTTP GET request
    response = requests.get(url)O10/24/2023
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract the settlements data
        settlements = data.get('settlements', [])
        
        if settlements:
            # Print the table headers
            headers = settlements[0].keys()
            print("\t".join(headers))

            # Print the settlement details for each contract
            for settlement in settlements:
                values = [str(settlement[key]) for key in headers]
                print("\t".join(values))
        else:
            print("No settlement data found for the specified date.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Date Format MM/DD/YYYY   eg. '10/24/2023'
settlement_date=input("Enter Settlement date MM/DD/YYYY\n")
get_settlement_details(settlement_date)