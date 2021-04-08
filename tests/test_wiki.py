from ppbot.apis.wiki import Wiki
import urllib.request


def test_get_wiki_result(monkeypatch):
    result = "Tu sais que Le Jardin Botanique de Tours " \
             "est situé à l'Ouest de la ville boulevard Tonnellé, " \
             "face à la l'hôpital Bretonneau. " \
             "Il est implanté sur une ancienne zone humide " \
             "traversée autrefois par le ruisseau Sainte-Anne. " \
             "Ce cours d'eau reliait directement la Loire et " \
             "le Cher et alimentait les douves du château de Plessis-lès-Tours.."
    wikiped = Wiki("jardin botanique tours")
    monkeypatch.setattr(urllib.request, 'urlopen', result)
    assert wikiped.get_wiki_result() == result
