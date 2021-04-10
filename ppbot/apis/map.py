import requests
from usekey import key_maps


class Map:
    """
    Class to:
     - find the geocode from a place through the user input question
     - find an address after getting the geocode
    """
    def __init__(self, question):
        """
        Initialize the api_key, the url, and the question input to build the API
        """
        self.geocode_base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.question = "".join(question)
        self.geo_key = key_maps

        self.alternative_ad = "Lotus Temple Rd, Bahapur, " \
                              "Shambhu Dayal Bagh, Kalkaji, " \
                              "New Delhi, Delhi 110019, Inde"
        self.alternative_geo = {'lat': 28.553746427467193,
                                'lng': 77.2588800416219}

    def geocode(self):
        """
        Method to find the latitude and longitude
        of a place answering to the user's question parsed
        """
        param = {"address": self.question,
                 "key": self.geo_key
                 }
        response = requests.get(self.geocode_base_url, params=param)
        answer_json = response.json()
        try:
            search_geocode = answer_json['results'][0]['geometry']['location']
            if answer_json['status'] in ['OK', 'ZERO_RESULTS']:
                return search_geocode
        except IndexError:
            return self.alternative_geo

    def get_address_from_geocode(self):
        """
        Method to find the exact address after getting the geocode
        """
        param = {"address": self.question,
                 "key": self.geo_key
                 }
        response = requests.get(self.geocode_base_url, params=param)
        answer_json = response.json()
        try:
            search_address = answer_json['results'][0]['formatted_address']
            if answer_json['status'] in ['OK', 'ZERO_RESULTS']:
                return search_address
        except IndexError:
            return self.alternative_ad
