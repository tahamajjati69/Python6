

import pytest
from film import Film, films_to_json, films_from_json


def test_creation_valide():
    f = Film("Inception", "Christopher Nolan", 2010, 8.8)
    assert f.titre == "Inception"
    assert f.note == 8.8


def test_note_invalide():
    with pytest.raises(ValueError):
        Film("Test", "A", 2000, 12)


def test_annee_invalide():
    with pytest.raises(TypeError):
        Film("Test", "A", "1999", 8)


def test_to_json():
    f = Film("Matrix", "Wachowski", 1999, 9.0)
    js = f.to_json()
    assert '"note": 9.0' in js


def test_from_json():
    f1 = Film("Matrix", "Wachowski", 1999, 9.0)
    f2 = Film.from_json(f1.to_json())
    assert f1 == f2


def test_est_classique():
    assert Film("A", "B", 1995, 7).est_classique() is True
    assert Film("A", "B", 2005, 7).est_classique() is False


def test_comparaison():
    f1 = Film("A", "B", 2010, 6.0)
    f2 = Film("A", "B", 2010, 8.0)
    assert f1 < f2


def test_favoris_json():
    films = [
        Film("Film1", "X", 1995, 7),
        Film("Film2", "Y", 2020, 9)
    ]
    js = films_to_json(films)
    rec = films_from_json(js)
    assert rec == films
