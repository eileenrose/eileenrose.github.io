
def SayHello(name, day, fruits):
    print "Hello {name}, how are you?".format(name=name)
    print "The day of the week is: {day_of_week}".format(day_of_week=day)
    for fruit in fruits:
        print "You like {fruit}".format(fruit=fruit)

SayHello("John", "Friday", [1,"watermelon","mangos"])


def SomeFunctionYouWillWrite(food):
    if food.lower() == "fries":
        return food
    food = food.upper()
    vowels =['A','E','I','O','U']
    for vowel in vowels:
        food = food.replace(vowel, vowel*3)
    return food

for i in range(0, 3):
    food = raw_input("What is favorite food? ")
    food = SomeFunctionYouWillWrite(food)
    print food

groceries_by_price = {'ham':3.25, 'butter': 1.15}
for item in groceries_by_price:
    print "{item} costs {price}".format(item=item, price=groceries_by_price[item]) # variable = key

if 'butter' in groceries_by_price:
    print 'We have butter'

if 'kale' in groceries_by_price:
    print 'We have kale'
else:
    print 'We do not sell kale'

sandwiches = [ ["sourdough", "cheese", "ham"], ["wheat", "tomato", "bacon"] ]
print sandwiches[0]
print sandwiches[1][0]

for sandwich in sandwiches:
    print "Sandwich start"
    for ingredient in sandwich:
        print "Ingredients is: {ingredient}".format(ingredient=ingredient)
    print "Sandwich end"





contacts = {'seattle':{'mayor':'mayor@12thman.com', 'ofp':'cofp@12thman.com'}, 'nyc':{} }
print contacts['nyc'] #prints back an empty dictionary
print contacts['seattle']['mayor']
for roles in contacts['seattle']:
    print roles

cities = {"Seattle":{"Mayor":"Ed Murray", "Population":"652405", "Website":"http://www.seattle.gov/"}, "New York":{"Mayor":"Bill de Blasio", "Population":"8406000", "Website":"http://www.ny.gov/"}, "Houston":{"Mayor":"Sylvester Turner", "Population":"2196000", "Website":"http://www.houstontx.gov/"} }
for city in cities:
    print "City: " + city
    for info in cities["Seattle"]:

class Automobile:
    def __init__(self, color, brand, number_of_doors):
        self.color = color
        self.brand = brand
        self.number_of_doors = number_of_doors

    def washme(self):
        print "I got washed, I am shiny and {color}".format(color=self.color)

    def equals(self, other):
        return self.color == other.color and self.brand == other.brand and self.number_of_doors == other.number_of_doors


wreck = Automobile("green", "Honda", 4)
daily = Automobile("red", "Ferrari", 2)
print wreck.color
print daily.brand
wreck.washme()
print wreck.equals(daily)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance+= amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print "Your balance is: {balance}".format(balance=self.balance)


account = BankAccount(10000)
account.print_balance()
balance = account.deposit(500)
print "Current balance is: " +str(balance)
#account.print_balance
#account.withdraw(4000)
#account.print_balance()

import random

dice = random.randint(1, 6)
print "Rnadom dice throw: {dice}".format(dice=dice)


class Auto:
    def __init__(self, color):
        self.color = color

    def washme(self):
        print "I got washed... I am " + self.color

car = Auto('green')
car.washme()
