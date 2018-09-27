#fortune cookie
import random

print("Will you win the case?")

fortune = random.randint(1,3)

if fortune == 1:
    print("possibly")
elif fortune == 2:
    print("ofcourse")
elif fortune == 3:
    print("time to find a new job")
