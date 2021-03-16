import requests
import yaml


class Map:
    """
    Class to:
     - find the geocode from a place through the user input question
     - find an address after getting the geocode
    """
    def __init__(self, question):
        """ Initialize the api_key, the url, and the question input to build the API"""
        self.geocode_base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        self.question = "".join(question)

    def yaml_loader(self, filepath):
        """Loads the the API key for the geocoding with a yaml file"""
        with open(filepath, "r") as file:
            self.api_key = yaml.load(file, Loader=yaml.FullLoader)
            for name, value in self.api_key.items():
                return name, value

    def geocode(self):
        """ Method to find the lattitude and longitude of a place answering to the user's question criteria"""
        get_key = self.yaml_loader("apis/geokey.yaml")
        param = {"address": self.question,
                 "key": get_key}
        response = requests.get(self.geocode_base_url, params=param)
        answer_json = response.json()
        search_geocode = answer_json['results'][0]['geometry']['location']
        if answer_json['status'] in ['OK', 'ZERO_RESULTS']:
            return search_geocode
        raise Exception(answer_json['error_message'])

    def get_address_from_geocode(self):
        """ Method to find the exact address after getting the geocode"""
        get_key = self.yaml_loader("apis/geokey.yaml")
        param = {"address": self.question,
                 "key": get_key}
        response = requests.get(self.geocode_base_url, params=param)
        answer_json = response.json()
        search_geocode = answer_json['results'][0]['formatted_address']
        if answer_json['status'] in ['OK', 'ZERO_RESULTS']:
            return search_geocode
        raise Exception(answer_json['error_message'])
