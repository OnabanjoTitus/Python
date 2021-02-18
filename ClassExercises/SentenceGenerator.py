import random

articles = ["the", "a", "one", "some", "any"]
nouns = ["boy", "girl", "dog", "town", "car"]
verbs = ["drove", "jumped", "ran", "walked", "skipped"]
prepositions = ["to", "from", "over", "under", "on"]


def getSentence():
    sentence = ""
    space = " "
    randomNumber = random.randint(0, 4)
    sentence += articles[randomNumber].capitalize()
    sentence += space
    randomNumber = random.randint(0, 4)
    sentence += nouns[randomNumber].capitalize()
    sentence += space
    randomNumber = random.randint(0, 4)
    sentence += verbs[randomNumber].capitalize()
    sentence += space
    randomNumber = random.randint(0, 4)
    sentence += prepositions[randomNumber].capitalize()
    sentence += space
    randomNumber = random.randint(0, 4)
    sentence += articles[randomNumber].capitalize()
    sentence += space
    randomNumber = random.randint(0, 4)
    sentence += nouns[randomNumber].capitalize()
    sentence += "."
    print(sentence)


def main():
    for i in range(0, 20):
        getSentence()


if __name__ == '__main__':
    main()
