from ppbot.apis.map import Map
import urllib.request


def test_geocoding_result_from_def_geocode_mock(monkeypatch):
    result = {'lat': 44.0774541, 'lng': 3.0228388}
    gmap = Map("millau viaduc")
    monkeypatch.setattr(urllib.request, 'urlopen', result)
    assert gmap.geocode() == result


def test_address_result_from_def_get_address_from_geocode_mock(monkeypatch):
    result = "Jardin botanique de Tours, 33 Boulevard Tonnellé, 37000 Tours, France"
    gmap = Map("Jardin Botanique Tours")
    monkeypatch.setattr(urllib.request, 'urlopen', result)
    assert gmap.get_address_from_geocode() == result





