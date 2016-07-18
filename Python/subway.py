# A subway story

# You hop on the subway at Union Square. As you are waiting for the train you
# take a look at the subway map. The map is about 21 inches wide and 35 inches
# tall. Let's write a function to return the area of the map:
def map_size(width, height):
    map_area = width * height
    return "The map is %d square inches" % (map_area)

# Now you give it a shot! It takes about 156 seconds to go between stops and
# you'll be taking the train for 3 stops. Write a function that calculates how
# long your trip will take.
def trip_length(seconds, numberOfTrips):
  #  put your code here
  return str(seconds * numberOfTrips) + " seconds"


# The train arrives and you hop on. Guess what time it is? It's showtime! There
# are 23 people on the train and each person gives the dancers 1.5 dollars.
# Write a function that returns how much money they made.

def dancer_money(dollars, dancers):
    return "${:,.2f}".format((dollars * dancers))
    #return "$%.2f" % (dollars*dancers)

# There is one grumpy lady on the train that doesn't like the dancing though.
# Write a function called stop_dancing that returns a message to the dancers in
# all caps.

def noFunAllowed():
    return "STOP DANCING!"


# There is also a really enthusiastic rider who keeps shouting "Everything is
# awesome!" Write a function that returns everything is awesome 5 times.

def thatOneGuy():
    p = "Everything is awesome! "*5
    return p


# You are almost at your stop and you start thinking about how you are going to
# get home. You have $18 left on your metro card. Write a function that returns
# how many trips you have left.

def budgetPlanning(fare, money_left):
    return money_left / fare


# ${:0,.2f}'.format(184467616.1)

# Call your functions below:
print "How big is that subway map?"
# Call your function here - like this:
print map_size(21, 35)
# ... but that doesn't output anything. Hmm. See if you can fix it.

print "This is how long the trip will take"
print trip_length(156, 3)

print "How much money did the train dancers make?"
# call your function here
print dancer_money(1.5, 23)

print "That lady told the train dancers to"
# call your function here
print noFunAllowed()

print "That guy kept shouting"
# call your function here
print thatOneGuy()

print "This is how many trips I have left on my metrocard"
# call your function here
print budgetPlanning(2, 18)

"""
import practice2

from practice2 import Auto
car = practice2.Auto("Green")
car.washme()
"""
