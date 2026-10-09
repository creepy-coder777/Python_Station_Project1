import random

templates = [
    "It was about {number} {time} ago when I arrived at the hospital in a {transport}. "
    "The hospital is a {adjective} place, there are a lot of {adjective2} {noun} here. "
    "There are nurses here who have {color} {body_part}. "
    "If someone wants to come into my room I told them that they have to {verb} first. "
    "I’ve decorated my room with {number2} {noun2}. "
    "Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
    "I heard that all doctors {verb2} {noun4} every day for breakfast. "
    "The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!"
]

tmpl = random.choice(templates)

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

story = tmpl.format(
  number=number, time=time, transport=transport, adjective = adjective,
  adjective2=adjective2, noun=noun, color=color, body_part=body_part,verb=verb,
  number2=number2, noun2=noun2, noun3=noun3, body_part2=body_part2, verb2=verb2, noun4=noun4, 
  adjective3=adjective3, silly_word=silly_word, noun5=noun5 
  )
print(story)