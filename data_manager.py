import requests
import os

SHEET_ENDPOINT_PRICES = os.getenv("SHEET_ENDPOINT_PRICES")
SHEETY_ENDPOINT_USERS = os.getenv("SHEETY_ENDPOINT_USERS")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT_PRICES)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT_PRICES}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_ENDPOINT_USERS)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
