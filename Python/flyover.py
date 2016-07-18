
def fasten_seatbelts():
    print "Fasten your seatbelts. Or not. Just don't sue us if you die."

def free_to_move_about_the_cabin():
    print "Feel free to move about now. And keep the bathroom door closed."

def ca(b):
    print "We are flying over " + b

def nv(b):
    print "We are flying over " + b

def ut(b):
    print "We are flying over " + b
def co(b):
    print "We are flying over " + b
def ks(b):
    print "We are flying over " + b
def mo(b):
    print "We are flying over " + b
def il(b):
    print "We are flying over " + b
def ind(b):
    print "We are flying over " + b
def oh(b):
    print "We are flying over " + b
def pa(b):
    print "We are flying over " + b
"""
def stateFlying(states):
    for state in states:
        fasten_seatbelts()
        print "We are flying over " + state
        free_to_move_about_the_cabin()



state = ['Pennsylvania', 'Ohio', 'Indiana', 'Illnois', 'Missouri', 'Kansas', 'Colorado', 'Utah', 'Nevada', 'California']
stateFlying(state)
"""

fasten_seatbelts()
free_to_move_about_the_cabin()
pa('Pennsylvania')
oh('Ohio')
ind('Indiana')
il('Illnois')
mo('Missouri')
ks('Kansas')
co('Colorado')
ut('Utah')
nv('Nevada')
ca('California')

print "My favorite state is New York."
leastFavorite = ['Quebec', 'Ontario', 'Alberta']
lf = "My least favorite states are "
for districts in leastFavorite:
    lf += districts[::-1] + " "
print lf
