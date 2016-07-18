# Happy Parrot - This parrot is so happy. It accepts a 'thing' as its argument and then returns a string where it says how happy it is about the thing!
def happy_parrot(thing):
  return "I am so happy about %s!" %(thing)

print happy_parrot('carrots')

# Boring Parrot - Write a method for a boring parrot that just returns whatever string you give him as an argument.
def boring_parrot(bored):
    return bored

# Math Parrot - Create a method that accepts two numbers as arguments and adds them together!
def math_parrot(num1, num2):
    return num1+num2


# Friendly Parrot - This parrot greets people by returning their name and age (don't forget to pass that information in as arguments).
def friendly_parrot(name, age):
    return "Hello {name}! You are {age}.".format(name=name, age=age)


# Favorites Parrot - Tell this parrot about your three favorite things and he will return "I love <that thing> too!" for each of them.
def favorites_parrot():
    ugh ="I love "
    for i in range(0,3):
        thing = raw_input("What is your favorite thing? ")
        if (i == 2):
            ugh += thing + " "
        else:
            ugh += thing + ", "
    return ugh + "too!"


# Now try calling your methods below with any arguments of your choice and puts them to the screen. Like this:
print happy_parrot("waffles")
# call your methods here
print boring_parrot("FAQ")
print math_parrot(3,4)
print friendly_parrot("Bob",78)
print favorites_parrot()


# Now let's pretend you are a wizard and you want to place a spell on each of the parrots so that they speak backwards. How would you do that?
def reverseSpeak():
    print happy_parrot("waffles")[::-1]
    print boring_parrot("FAQ")[::-1]
    print math_parrot(3,4)
    print friendly_parrot("Bob",78)[::-1]
    print favorites_parrot()[::-1]

reverseSpeak()


"""
def reverse(speak):
    return speak[::-1]

print reverse(happy_parrot("pie"))
print reverse(str(math_parrot(12,12)))
"""




# The spell has been broken and everyone is speaking normally again. The parrots are really excited about it though - make them shout in all caps.

def excitement():
    print happy_parrot("waffles").upper()
    print boring_parrot("FAQ").upper()
    print math_parrot(3,4)
    print friendly_parrot("Bob",78).upper()
    print favorites_parrot().upper()

excitement()
