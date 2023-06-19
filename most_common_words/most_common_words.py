import os


def get_common_words():
    try:
        path = os.path.join('most_common_words', 'common.txt')
        data = open(path)

        words_with_quantity = {}

        for line in data:
            words = line.replace('\n', '').replace(
                ".", "").replace(",", "").lower().split(" ")

            for word in words:
                words_with_quantity[word] = words_with_quantity.get(
                    word, 0) + 1

        sorted_words = sorted(list(words_with_quantity))

        for k in sorted_words:
            print(f"A palavra {k} apareceu {words_with_quantity[k]} vezes.")

    except:
        print("something went wrong")


get_common_words()
