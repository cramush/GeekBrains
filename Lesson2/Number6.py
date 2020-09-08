quantity = int(input("Введи количество товара: "))
i = 1
dictionary = []
line = []
analytics = {}

while i <= quantity:
    dictionary = dict({"Название": input("\nВведи название "), "Цена": input("Введи цену "),
                       "Количество": input("Введи количество "), "Ед": input("Введи единицу измерения ")})
    line.append((i, dictionary))
    i += 1
    analytics = dict({"Название": dictionary.get("Название"), "Цена": dictionary.get("Цена"),
                      "Количество": dictionary.get("Количество"), "Ед": dictionary.get("Ед")})
print("\n", line)
