from film import Film, films_to_json, films_from_json

def main():
    print("=== Test classe Film ===\n")

    film1 = Film("Inception", "Christopher Nolan", 2010, 8.8)
    print("Film 1 :", film1)

    js = film1.to_json()
    print("\nJSON :", js)

    film2 = Film.from_json(js)
    print("\nRechargé depuis JSON :", film2)

    print("\nEst classique ? :", film2.est_classique())

    film3 = Film("Le Parrain", "Francis Ford Coppola", 1972, 9.2)
    print("\nComparaison :")
    print("Inception < Le Parrain ?", film1 < film3)

    favoris = [film1, film3]
    favoris_json = films_to_json(favoris)
    print("\nFavoris JSON :", favoris_json)

    favoris_reload = films_from_json(favoris_json)
    print("\nFavoris rechargés :", favoris_reload)


if __name__ == "__main__":
    main()
