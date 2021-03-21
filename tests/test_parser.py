from ppbot.parser import Parser

parse = Parser("ppbot/words.json")


def test_the_parsing_from_a_sentence():
    user_input = "Est-ce que tu connais " \
            "l'adresse d'OpenClassrooms ?"
    assert parse.answer_parser(user_input) == "openclassrooms"