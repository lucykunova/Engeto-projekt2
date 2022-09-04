import random

ODDELOVAC = "=" * 30
print("Hi there!")
print(ODDELOVAC)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(ODDELOVAC)

def vyber_cisla(cislo):
  return [int(i) for i in str(cislo)]

def bez_duplikatu(cislo):
  hadane_cislo = vyber_cisla(cislo)
  if len(hadane_cislo) == len(set(hadane_cislo)):
    return True
  else:
    return False

def generuj_cislo():
  while True:
    cislo = random.randint(1000,9999)
    if bez_duplikatu(cislo):
      return cislo

def pocet_bullscows(cislo,tip):
  bull_cow = [0,0]
  hadane_cislo = vyber_cisla(cislo)
  tip_hrace = vyber_cisla(tip)
  
  for i,j in zip(hadane_cislo,tip_hrace):
    if j in hadane_cislo:
      if j == i:
        bull_cow[0] += 1
      else:
        bull_cow[1] += 1

  return bull_cow

cislo = generuj_cislo()
pokusy =int(input("Enter number of tries: "))

while pokusy > 0:
  tip = int(input("Enter your guess: "))

  if not bez_duplikatu(tip):
    print("Number should not have more than 1 of the same digits. Try again.")
    continue
  if tip < 1000 or tip > 9999:
    print("Enter a 4 digit number only. Try again.")
    continue
	
  bull_cow = pocet_bullscows(cislo,tip)
  pokusy -= 1

  if bull_cow[0] == 1 and bull_cow[1] == 1:
    print(f"{bull_cow[0]} bull, {bull_cow[1]} cow")
    print(ODDELOVAC)
  elif bull_cow[0] == 1 and bull_cow[1] != 1:
    print(f"{bull_cow[0]} bull, {bull_cow[1]} cows")
    print(ODDELOVAC)
  elif bull_cow[0] != 1 and bull_cow[1] == 1:
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cow")
    print(ODDELOVAC)
  else:
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    print(ODDELOVAC)

  if bull_cow[0] == 4:
    print("You guessed right in {pokusy} tries!")
    break

else:
  print(f"You ran out of tries. Number was {cislo}")
