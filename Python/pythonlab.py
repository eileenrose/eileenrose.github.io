
import random


def speak_to_walle(response):
    if response == "BYE"*3:
        return
    elif response == response.upper():
            print "EEEEEEEEEEEVAAAAAAAAAA!"
    else:
        print "Dirrrrr-ect-tivvve?"
    print random.randint(1,101)

stop_walle = 1
while stop_walle == 1:
    response = raw_input("Talk to Wall-E! ")
    speak_to_walle(response)
    if response == "BYE"*3:
        stop_walle+=1


pyramid = [ "   #  #   ", "  ##  ##  ", " ###  ### ", "####  ####"]
for pyr in pyramid:
    print pyr

height = int(raw_input("How tall is your pyramid? "))
if height > 23 or height < 0:
    print "That is not a valid height."
    exit(1)
repeat = int(raw_input("How many times would you like to repeat? "))

pyramid_user = []

for r in range (0, repeat):
    if r % 2 == 0:
        n = 1
        j = height - 1
        for var in range(0, height):
            pyramid_user.append(" "*(height-n) + "#"*(height - j) + "  " + "#"*(height-j) + " "*(height-n))
            n+=1
            j -= 1
    else:
        n = 0
        j = height
        for var in range(0, height):
            pyramid_user.append(" "*(height-j) + "#"*(height - n) + "  " + "#"*(height-n) + " "*(height-j))
            n += 1
            j -= 1


for py in pyramid_user:
    print py
