import random

words_with_hints = {
    "apple": [
        "It's a fruit.",
        "It can be red, green, or yellow.",
        "It keeps the doctor away.",
        "It grows on trees.",
        "It's often eaten raw.",
        "Has seeds inside.",
        "Common in lunch boxes.",
        "You can make juice from it.",
        "Used in pies.",
        "A forbidden fruit in some stories."
    ],
    "tiger": [
        "It's an animal.",
        "A big cat.",
        "It has orange fur.",
        "It has black stripes.",
        "It lives in the jungle.",
        "Carnivorous predator.",
        "Known for its roar.",
        "National animal of India.",
        "A symbol of strength.",
        "It can swim well."
    ],
    "house": [
        "It's a building.",
        "People live in it.",
        "It has doors and windows.",
        "It gives shelter.",
        "It can be big or small.",
        "Often has bedrooms and kitchen.",
        "Made of bricks or wood.",
        "You decorate it.",
        "Protects you from weather.",
        "Has a roof."
    ],
    "beach": [
        "It's a place.",
        "Next to a sea or ocean.",
        "Has sand.",
        "People relax here.",
        "You can sunbathe.",
        "You can swim here.",
        "Good for building sandcastles.",
        "Popular for vacations.",
        "Has waves and shells.",
        "Often has palm trees."
    ],
    "grape": [
        "It's a fruit.",
        "Small and round.",
        "Can be green or purple.",
        "Grows in bunches.",
        "Very juicy.",
        "Sweet or sour taste.",
        "Used to make wine.",
        "Can be dried into raisins.",
        "Found in fruit salads.",
        "Often eaten as snacks."
    ]
}

word, hints = random.choice(list(words_with_hints.items()))
tries = 10
guessed = []
hint_index = 0

print("🎮 Welcome to Hangman!")
print("Hint 1:", hints[hint_index]) 

while tries > 0:
    display = "".join([l if l in guessed else "_ " for l in word])
    print("\nWord:", display)

    if display == word:
        print("🎉 You won!")
        break

    g = input("Guess a letter: ").lower()
    if g in guessed:
        print("Already guessed that letter.")
    else:
        guessed.append(g)
        if g not in word:
            tries -= 1
            print("❌ Wrong! Tries left:", tries)
        else:
            print("✅ Good guess!")

    display = "".join([l if l in guessed else "_ " for l in word])
    
    if display != word:
        hint_index += 1
        if hint_index < len(hints):
            print(f"Hint {hint_index + 1}:", hints[hint_index])
    else:
        print("🎉 You won!")
        break

if display != word:
    print("💀 You lost! The word was:", word)
