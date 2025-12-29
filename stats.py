def number_of_words(words):
    number = len(words.split())
    return number

def number_of_characters(words):
    count_charaters = {}
    lowercased_words = words.lower()

    for characters in lowercased_words:
        if characters in count_charaters:
            count_charaters[characters] += 1
        else:
            count_charaters[characters] = 1
    return count_charaters

def book_report(characters):
    sorted_characters = []
    for c in characters:
        if c.isalpha():
            sorted_characters.append({"char": c, "num": characters[c]})
    sorted_characters.sort(reverse=True, key=sort_on)
    for item in sorted_characters:
        print(item["char"]+":", item["num"])


def sort_on(items):
    return items["num"]