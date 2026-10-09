import random

templates = [
    "It was about {number} {time} ago when I arrived at the hospital in a {transport}. "
    "The hospital is a {adjective} place, there are a lot of {adjective2} {noun} here. "
    "There are nurses here who have {color} {body_part}. "
    "If someone wants to come into my room I told them that they have to {verb} first. "
    "I’ve decorated my room with {number2} {noun2}. "
    "Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
    "I heard that all doctors {verb2} {noun4} every day for breakfast. "
    "The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!",

    "This weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}. "
    "I am so {emotion} to {verb} in a tent. I am {emotion2} we might see a(n) {animal}, I hear they’re kind of dangerous. "
    "While we’re camping, we are going to hike, fish, and {verb2}. "
    "I have heard that the {color} lake is great for {verb_ing}. "
    "Then we will {adverb_ly} hike through the forest for {number} {time}. "
    "If I see a {color} {animal} while hiking, I am going to bring it home as a pet! "
    "At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!",

    "Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest. "
    "I found myself here one day after going for a ride on a {color} {animal} in {place}. "
    "There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here! "
    "In the {room} there is a pool full of {noun}. "
    "I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. "
    "It feels as though I have lived here for {number} {time}. "
    "I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"
]


number = input("Input a number: ")
time = input("Input a measure of time: ")
transport = input("Input a mode of transportation: ")
adjective = input("Input an adjective: ")
adjective2 = input("Input another adjective: ")
noun = input("Input a noun: ")
color = input("Input a color: ")
body_part = input("Input a body part: ")
verb = input("Input a verb: ")
number2 = input("Input another number: ")
noun2 = input("Input another noun: ")
noun3 = input("Input another noun: ")
body_part2 = input("Input another body part: ")
verb2 = input("Input another verb: ")
noun4 = input("Input another noun: ")
adjective3 = input("Input another adjective: ")
silly_word = input("Input a silly word: ")
noun5 = input("Input another noun: ")
proper_noun = input("Input a proper noun(person's name): ")
emotion = input("Input an adjective (feeling): ")
emotion2 = input("Input another adjective (feeling): ")
animal = input("Input an animal: ")
verb_ing = input("Input a verb (ending in ing): ")
adverb_ly = input("Input an adverb (ending in ly): ")
place = input("Input a place: ")
magical_creature = input("Input a magical creature (plural): ")
magical_creature2 = input("Input another magical creature (plural): ")
room = input("Input a room in a house: ")
noun_plural3 = input("Input a noun (plural): ")
noun_plural4 = input("Input another noun (plural): ")
adjective4 = input("Input another adjective: ")
adjective5 = input("Input another adjective: ")


def play_madlibs():
  print("=" * 20)
  print("Welcome to the Mad Libs Game!")
  print("=" * 20)
  print("Select a story template:")
  print("1. Hospital Visit")
  print("2. Camping Trip")
  print("3. Enchanted Castle")
  print("4. Random Choice!")
    
  choice = input("\nEnter your choice (1-4): ").strip()
  if choice == "1":
    tmpl = templates[0]
  elif choice == "2":
    tmpl = templates[1]
  elif choice == "3":
    tmpl = templates[2]
  elif choice == "4":
    tmpl = random.choice(templates)
  story = tmpl.format(
    number=number, time=time, transport=transport, adjective = adjective,
    adjective2=adjective2, noun=noun, color=color, body_part=body_part,verb=verb,
    number2=number2, noun2=noun2, noun3=noun3, body_part2=body_part2, verb2=verb2, noun4=noun4,
    adjective3=adjective3, silly_word=silly_word, noun5=noun5, adverb_ly=adverb_ly, place=place,
    magical_creature=magical_creature, magical_creature2=magical_creature2, room=room,
    noun_plural3=noun_plural3, noun_plural4=noun_plural4, adjective4=adjective4, adjective5=adjective5,
    )
  print(story)

if __name__ == "__main__":
  play_madlibs()