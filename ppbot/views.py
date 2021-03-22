from flask import render_template, jsonify, request

from . import app

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    print("la requête est", user_text)
    return jsonify(['pas de réponse'])
