from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not (0 <= self.note <= 10):
            raise ValueError("La note doit être entre 0 et 10.")
        if not isinstance(self.annee, int):
            raise TypeError("L'année doit être un entier.")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    def __lt__(self, other):
        if not isinstance(other, Film):
            return NotImplemented
        return self.note < other.note

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Film(**data)


def films_to_json(films: list[Film]) -> str:
    """Sérialiser une liste de films."""
    return json.dumps([asdict(f) for f in films], ensure_ascii=False)


def films_from_json(json_str: str) -> list[Film]:
    """Recharger une liste de films depuis du JSON."""
    data = json.loads(json_str)
    return [Film(**item) for item in data]
