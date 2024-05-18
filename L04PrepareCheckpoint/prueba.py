import random

def main():
    for _ in range(6):
        make_sentence()

def make_sentence():
    single_quantity = [1, 1, 1]
    plural_quantity = [2, 2, 2]
    
    tenses = ["past", "present", "future"]
    
    # Single quantities
    for tense in tenses:
        sentence = f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1, tense)} {get_prepositional_phrase(1)}."
        print(sentence)
    
    # Plural quantities
    for tense in tenses:
        sentence = f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2, tense)} {get_prepositional_phrase(2)}."
        print(sentence)

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

def get_verb(quantity, tense):
    if tense == "past":
        if quantity == 1:
            words = ["drank", "ate", "grew", "laughed", "thought", "ran", "walked", "talked"]
        else:
            words = ["drank", "ate", "grew", "laughed", "thought", "ran", "walked", "talked"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "walks", "talks"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "walk", "talk"]
    else: # future
        if quantity == 1:
            words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will walk", "will talk"]
        else:
            words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will walk", "will talk"]
    return random.choice(words)

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

if __name__ == "__main__":
    main()
