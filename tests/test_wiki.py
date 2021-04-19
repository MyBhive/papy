from ppbot.apis.wiki import Wiki
import urllib.request


def test_get_wiki_result(monkeypatch):
    result = "Alors alors! A ce que je comprends, " \
             "tu veux l'endroit à cette adresse: " \
             "Jardin botanique de Tours, 33 Boulevard Tonnellé, " \
             "37000 Tours, France? " \
             "Non mais tu sais que Le Jardin Botanique de Tours " \
             "est situé à l'Ouest de la ville boulevard Tonnellé, " \
             "face à la l'hôpital Bretonneau. " \
             "Il est implanté sur une ancienne zone humide " \
             "traversée autrefois par le ruisseau Sainte-Anne.."
    wikiped = Wiki("jardin botanique tours",
                   "Jardin botanique de Tours, 33 Boulevard Tonnellé, 37000 Tours, France",
                   {'lat': 47.3868187, 'lng': 0.6663859999999999})
    monkeypatch.setattr(urllib.request, 'urlopen', result)
    assert wikiped.get_wiki_result() == result
