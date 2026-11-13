# # string concatenation (aka how to put strings together)
# # suppose we want to create astring that says "subscribe to _____"
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! it makes me so excited all the time because\
    i love to{verb1}. dtay hydrated and {verb2} like  you are {famous_person}"

print(madlib)