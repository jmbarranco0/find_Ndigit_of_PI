# @Author Jose Manuel Flores Barranco

from decimal import Decimal
## We import the decimal library for high precision decimals ##

# This is PI #
realPI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

## We will use the Nilakantha Series method for this calculation https://en.wikipedia.org/wiki/Pi ##

####### NILAKANTHA SERIES #########

def nDigitsOfPI(repetitions):
  pi = Decimal(3.0)
  op = 1
  n = 2
  for n in range (2, 2*repetitions+1,2):
    pi += 4/Decimal(n*(n+1)*(n+2)*op)
    op *= -1
  return pi

####### NILAKANTHA SERIES #########


nDigits = int(input("Enter the ammount of decimals you want to compute:"))
print("\nHow many times do you want to iterate? The greater of this, the better aproximation you'll get -and the lower it gets-")

## We ask for how many precise the user wants the algorithm to be ##
repetitions = int(input("\nRepetitions: "))

## Now we shrink the number just for visual concerns ##
result = str(nDigitsOfPI(repetitions))[0:2+nDigits]

## Now we compare to the real PI ##

print("My aproximation of PI for " + str(nDigits) + " is: " + result + "\n")

print("And this is PI with that many digits: " + realPI[:2+nDigits])
