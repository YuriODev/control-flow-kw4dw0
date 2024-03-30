# Your solution to Exercise 18
def convertible():       
  conv = input("Are you in a convertible with blah blah blah\n").upper()
  if conv == "YES":
    return "Say hi."
  else:
    return "Don't say hi."

def bank():
  rob = input("Are you robbing a bank?\n").upper()
  if rob == "YES":
    return "Don't say hi."
  else:
    robe = input("Are you in a bathrobe?\n").upper()
    if robe == "YES":
      return "Don't say hi."
    else:
      return "Say hi."

def ex():
  ex = input("Is it an ex?\n").upper()
  if ex == "YES":
    drunk = input("Are you drunk\n").upper()
    if drunk == "YES":
      rekindle = input("Do you want to rekindle?\n").upper()
      if rekindle == "YES":
        return "Say hi."
      else:
        return "Don't say hi."
    else:
      return convertible()
  else:
    fr_ex = input("Is it a friend's ex?\n").upper()
    if fr_ex == "YES":
      return "Don't say hi."
    else:
      en_or_fr = input("Are they an enemy or a frenemy?\n").upper()
      if en_or_fr == "YES":
        return convertible()

def unknown():
  flee = input("Is there time to flee?\n").upper()
  if flee == "YES":
    return "Run for it."
  else:
    phone = input("Could you pretend to get a call?\n").upper()
    if phone == "YES":
      return "Hello, doctor. What are my test results?"
    else:
      sungl = input("Are you wearing sunglasses?\n").upper()
      if sungl == "YES":
        return "Keep walking."
      else:
        return "Address the person using an amusing blahhhhh"

outcome = None

name = input("Do you remember their name?\n").upper()
if name == "YES":
  outcome = ex()
else:
  outcome = unknown()

print(outcome)
