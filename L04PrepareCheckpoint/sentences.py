import random

def main():
    tense = ["past", "present", "future","past", "present", "future",]
    quantity = [1, 1, 1, 2, 2, 2]

    for i in range(6):
        print(make_sentence(quantity[i], tense[i]))


def make_sentence(quantity,tenses):
    for tense in tenses:
        return f"{get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_adverb()} {get_prepositional_phrase(quantity)}."

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    return random.choice(words)


def get_preposition():
    p =  ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    return random.choice(p)

def get_prepositional_phrase(quantity):
    a = get_preposition() + " " + get_determiner(quantity) + " " + get_noun(quantity)
    return a

def get_adjective():
    adjectives = ["quick", "lazy", "sleepy", "noisy", "hungry", "happy", "sad", "angry", "tall", "short", "fat", "thin", "red", "blue", "green", "yellow", "bright", "dark", "long", "short"]
    return random.choice(adjectives)

def get_adverb():
    adverbs = ["quickly", "lazily", "sleepily", "noisily", "hungrily", "happily", "sadly", "angrily", "tall", "short", "fat", "thin", "red", "blue", "green", "yellow", "bright", "dark", "long", "short"]
    return random.choice(adverbs)

main()
