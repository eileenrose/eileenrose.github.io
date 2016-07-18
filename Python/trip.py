
destination = raw_input("What is your destination? (city.state/country) ")
dest = destination.split(".")
sites = raw_input("Where would you like to see? (add commas) ")
site = sites.split(",")
food = raw_input("What would you like to eat? (one meal) ").strip()
print "Your destination is " + dest[0].capitalize().strip() + ", " + dest[1].upper().strip()
for i in site:
    print "You will be visiting " + i.lstrip().capitalize()
print "You will be eating " + food
if len(site) < 5:
    print "You will be spending a night."
elif len(site) > 20:
    print "You will be spending 5 nights."
else:
    print "You will be spending 3 nights."

"""
city =raw_input("What city would you like to visit? ").capitalize()
question = raw_input("Is this an international city? [y/n ] ").lower()[0]
state_or_country = ""
sights = []
if question == "y":
    state_or_country = raw_input("What country will you be visiting? ").capitalize()
else:
    while True:
    state_or_country = raw_input("What state will you be visiting? ").upper()
    if len(state_or_country) == 2:
        break

while True:
    sight = raw_input("What sight would you like to visit? (PRESS ENTER TO END) ").title()
    if sight == "":
        break
    else:
        sights.append(sight)

food = raw_input("What would you like to eat during your trip? ").title()


print "Destination: {city}, {state}".format(city=city, state=state_or_country)
for sight int sights:
    print " - Visiting the: {sight}".format(sight=sights)
print "You will eat: {food}".format(food=food)
print "You will spend {count} days.".format(count=len(sights))
"""
