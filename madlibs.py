import random

templates = [
    "It was about {num} {time} ago when I arrived at the hospital in a {transport}. "
    "The hospital is a {adj} place, there are a lot of {adj2} {noun} here. "
    "There are nurses here who have {color} {body}. "
    "If someone wants to come into my room I told them that they have to {verb} first. "
    "I’ve decorated my room with {num2} {noun2}. "
    "Today I talked to a doctor and they were wearing a {noun3} on their {body2}. "
    "I heard that all doctors {verb2} {noun4} every day for breakfast. "
    "The most {adj3} thing about being in the hospital is the {silly_wrd} {noun5}!"
]

tmpl = random.choice(templates)

num = input("Input a number: ")
time = input("Input a measure of time: ")
transport = input("Input a mode of transportation: ")
adj = input("Input an adjective: ")
adj2 = input("Input another adjective: ")
noun = input("Input a noun: ")
color = input("Input a color: ")
body = input("Input a body part: ")
verb = input("Input a verb: ")
num2 = input("Input another number: ")
noun2 = input("Input another noun: ")
noun3 = input("Input another noun: ")
body2 = input("Input another body part: ")
noun4 = input("Input another noun: ")
adj3 = input("Input another adjective: ")
silly_wrd = input("Input a silly word: ")
noun5 = input("Input another noun: ")

story = tmpl.format(
  num=num, time=time, transport=transport, adj = adj,
  adj2=adj2, noun=noun, color=color, body=body,verb=verb,
  num2=num2, noun2=noun2, noun3=noun3, body2=body2, noun4=noun4, 
  adj3=adj3, silly_wrd=silly_wrd, noun5=noun5 
  )
print(story)