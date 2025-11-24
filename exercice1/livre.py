from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit: float):
        return Livre(
            titre=self.titre,
            auteur=self.auteur,
            annee=self.annee,
            prix=prix_reduit
        )

    def __lt__(self, other):
        if not isinstance(other, Livre):
            return NotImplemented
        return self.prix < other.prix


def livre_from_json(json_str: str) -> Livre:
    data = json.loads(json_str)
    return Livre(**data)


if __name__ == "__main__":
    livre1 = Livre("1984", "George Orwell", 1949, 9.90)
    print("JSON :", livre1.to_json())

    livre_promo = livre1.promo(7.99)
    print("Promo :", livre_promo)

    json_str = livre1.to_json()
    livre2 = livre_from_json(json_str)
    print("Reconstitué :", livre2)

    livreA = Livre("Livre A", "Auteur X", 2020, 15.0)
    livreB = Livre("Livre B", "Auteur Y", 2020, 12.0)
    print("B moins cher que A ?", livreB < livreA)
