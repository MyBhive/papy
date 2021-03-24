from flask import Flask, render_template, request, jsonify

from ppbot import parse
from ppbot.apis import map
from ppbot.apis import wiki

# from . import app ne fonctionne plus à partir du moment où j'importe mais autres fichiers .py
app = Flask(__name__)


@app.route("/", methods=["POST"])
@app.route("/index", methods=["POST"])
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def get_data():

    # get and parse the data
    parsing = parse.Parser("words.json")
    user_text = request.form["userText"]
    parse_text = parsing.answer_parser(user_text)
    print(parse_text)

    # get the gps coord and the address
    gmap = map.Map(parse_text)
    gps_coordinate = gmap.geocode()
    print(gps_coordinate)
    address = gmap.get_address_from_geocode()

    # get the wiki quote through the address
    wikip = wiki.Wiki(address)
    wiki_data = wikip.get_wiki_result()

    response = [wiki_data, gps_coordinate, address]
    return jsonify(response)
