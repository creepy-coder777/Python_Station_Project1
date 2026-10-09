import random

templates = [
    {
        "name": "Hospital Visit",
        "text": (
            "It was about {number} {time} ago when I arrived at the hospital in a {transport}. "
            "The hospital is a {adjective} place, there are a lot of {adjective2} {noun} here. "
            "There are nurses here who have {color} {body_part}. "
            "If someone wants to come into my room, I tell them that they have to {verb} first. "
            "I've decorated my room with {number2} {noun2}. "
            "Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
            "I heard that all doctors {verb2} {noun4} every day for breakfast. "
            "The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!"
        ),
        "words": [
            ("number", "Input a number"),
            ("time", "Input a measure of time"),
            ("transport", "Input a mode of transportation"),
            ("adjective", "Input an adjective"),
            ("adjective2", "Input another adjective"),
            ("noun", "Input a noun"),
            ("color", "Input a color"),
            ("body_part", "Input a body part"),
            ("verb", "Input a verb"),
            ("number2", "Input another number"),
            ("noun2", "Input another noun"),
            ("noun3", "Input another noun"),
            ("body_part2", "Input another body part"),
            ("verb2", "Input another verb"),
            ("noun4", "Input another noun"),
            ("adjective3", "Input another adjective"),
            ("silly_word", "Input a silly word"),
            ("noun5", "Input another noun"),
        ],
    },
    {
        "name": "Camping Trip",
        "text": (
            "This weekend I am going camping with {proper_noun}. "
            "I packed my lantern, sleeping bag, and {noun}. "
            "I am so {emotion} to {verb} in a tent. "
            "I am {emotion2} we might see a(n) {animal}; I hear they're kind of dangerous. "
            "While we're camping, we are going to hike, fish, and {verb2}. "
            "I have heard that the {color} lake is great for {verb_ing}. "
            "Then we will {adverb_ly} hike through the forest for {number} {time}. "
            "If I see a {color} {animal} while hiking, I am going to bring it home as a pet! "
            "At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!"
        ),
        "words": [
            ("proper_noun", "Input a person's name"),
            ("noun", "Input a noun"),
            ("emotion", "Input an adjective describing a feeling"),
            ("verb", "Input a verb"),
            ("emotion2", "Input another feeling adjective"),
            ("animal", "Input an animal"),
            ("verb2", "Input another verb"),
            ("color", "Input a color"),
            ("verb_ing", "Input a verb ending in -ing"),
            ("adverb_ly", "Input an adverb ending in -ly"),
            ("number", "Input a number"),
            ("time", "Input a measure of time"),
            ("silly_word", "Input a silly word"),
            ("noun2", "Input another noun"),
        ],
    },
    {
        "name": "Enchanted Castle",
        "text": (
            "Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest. "
            "I found myself here one day after going for a ride on a {color} {animal} in {place}. "
            "There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here! "
            "In the {room} there is a pool full of {noun}. "
            "I fall asleep each night on a {noun2} of {noun_plural3} "
            "and dream of {adjective4} {noun_plural4}. "
            "It feels as though I have lived here for {number} {time}. "
            "I hope one day you can visit, although the only way to get here now is "
            "{verb_ing} on a {adjective5} {noun5}!"
        ),
        "words": [
            ("proper_noun", "Input a person's name"),
            ("adjective", "Input an adjective"),
            ("color", "Input a color"),
            ("animal", "Input an animal"),
            ("place", "Input a place"),
            ("adjective2", "Input another adjective"),
            ("magical_creature", "Input a plural magical creature"),
            ("adjective3", "Input another adjective"),
            ("magical_creature2", "Input another plural magical creature"),
            ("room", "Input a room in a house"),
            ("noun", "Input a noun"),
            ("noun2", "Input another noun"),
            ("noun_plural3", "Input a plural noun"),
            ("adjective4", "Input another adjective"),
            ("noun_plural4", "Input another plural noun"),
            ("number", "Input a number"),
            ("time", "Input a measure of time"),
            ("verb_ing", "Input a verb ending in -ing"),
            ("adjective5", "Input another adjective"),
            ("noun5", "Input another noun"),
        ],
    },
]


def play_madlibs():
    print("=" * 30)
    print("Welcome to the Mad Libs Game!")
    print("=" * 30)

    print("""Select a story template:
          1. Hospital visit
          2. Camping trip
          3. Enchanted castle
          4. Random choice
          """)
    
    while True:
        choice = input("Choose your story (1-4): ").strip()

        if choice in ("1", "2", "3", "4"):
            break

        print("Invalid choice. Please enter a number from 1 to 4.")

    if choice == "4":
        template = random.choice(templates)
    else:
        template = templates[int(choice) - 1]

    print(f"\nLet's create your story: {template['name']}!\n")

    answers = {}

    for word_key, prompt in template["words"]:
        answers[word_key] = input(prompt + ":").strip()

    story = template["text"].format(**answers)
    print("\n" + "=" * 30)
    print("Your Madlibs story!!!")
    print(story)
    print("=" * 30)

if __name__ == "__main__":
    play_madlibs()