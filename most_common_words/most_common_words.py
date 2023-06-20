import os
import re as regEx


def get_common_words():
    try:
        path = os.path.join('most_common_words', 'common.txt')
        data = open(path)

        words_with_quantity = {}

        for line in data:
            words = regEx.sub('\.|\,|\\n', "", line)
            words = words.split(" ")

            for word in words:
                words_with_quantity[word] = words_with_quantity.get(
                    word, 0) + 1

        sorted_words = sorted(list(words_with_quantity))

        arr = []

        for k in sorted_words:
            arr.append({
                'word': k,
                'quantity': words_with_quantity[k]
            })

        arr.sort(key=lambda x: x['quantity'], reverse=True)

        for word in arr:
            print(
                f"A palavra {word['word']} apareceu {word['quantity']} vezes.")
    except:
        print("Something went wrong")
    finally:
        data.close()


get_common_words()
