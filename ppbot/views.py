from flask import render_template, request, jsonify

from ppbot import parse
from ppbot.apis import map
from ppbot.apis import wiki
from env import key_maps

from . import app


@app.route("/")
def index():
    """
    Through the framework flask, return the html file
    """
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def get_data():
    """
    - get and parse the data
    - get the gps coord and the address
    - get the wiki quote through the parse_text
    - return the response in json to send it to the front
    """
    # get and parse the data
    parsing = parse.Parser("ppbot/words.json")
    data = request.data.decode("utf-8")
    parse_text = parsing.answer_parser(data)
    print(parse_text)
    # get the gps coord and the address
    gmap = map.Map(parse_text)
    gps_coordinate = gmap.geocode()
    print(gps_coordinate)
    address = gmap.get_address_from_geocode()
    print(address)
    # get the wiki quote through the parse_text
    wiki_extract = wiki.Wiki(parse_text, address)
    wiki_data = wiki_extract.get_wiki_result()

    response = {"wiki": wiki_data, "coordinate": gps_coordinate, "address": address, "api_key": key_maps}
    print(response)
    return jsonify(response)
