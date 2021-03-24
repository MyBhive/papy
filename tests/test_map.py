from ppbot.apis.map import Map

gmap = Map("tour Eiffel")

def test_geocoding_result_from_def_geocode_mock(monkeypatch):
    result = {'lat': 48.9244592, 'lng': 2.3601645}

    def mock_urlopen():
        return result

    monkeypatch.setattr(
        "ppbot.apis.map.Map.geocode", mock_urlopen())
    assert result == {'lat': 48.9244592, 'lng': 2.3601645}


def test_address_result_from_def_get_address_from_geocode_mock(monkeypatch):
    result = "33 Boulevard Tonnelé France Tours 37000"

    def mock_url():
        return result

    monkeypatch.setattr(
        "ppbot.apis.map.Map.get_address_from_geocode", mock_url())
    assert result == "33 Boulevard Tonnelé France Tours 37000"




