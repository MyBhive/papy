from flask import render_template, request, jsonify

from ppbot import parse
from ppbot.apis import map
from ppbot.apis import wiki

from . import app



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def get_data():
    # get and parse the data
    parsing = parse.Parser("ppbot/words.json")
    user_text = request.form.get("user_text_form")
    parse_text = parsing.answer_parser(user_text)

    # get the gps coord and the address
    gmap = map.Map(parse_text)
    gps_coordinate = gmap.geocode()
    address = gmap.get_address_from_geocode()

    # get the wiki quote through the address or the parse_text?
    wiki_extract = wiki.Wiki(address)
    wiki_data = wiki_extract.get_wiki_result()

    response = {"wiki_quote": wiki_data, "geolo": gps_coordinate, "address": address}
    print(response)
    return jsonify(response)
