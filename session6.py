# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

# uName = "amr"
# uCountry = "canda"
# cName = "Python Course"
# cPrice = 100


      

# if uCountry == "Egypt":

#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

# elif uCountry == "KSA":

#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

# elif uCountry == "UK":

#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# else:

#   print(f"Hello {uName} Because You Are From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")


# ---------------
# -- Nested If --
# ---------------

# uName = "amr"
# isStudent = "Yes"
# uCountry = "Egypt"
# cName = "Python Course"
# cPrice = 100

# if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

#   if isStudent == "Yes":

#     print(f"Hi {uName} Because U R From {uCountry} And Student")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

#   else:

#     print(f"Hi {uName} Because U R From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


# elif uCountry == "Kuwait" or uCountry == "Bahrain":

#   print(f"Hi {uName} Because U R From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# else:

#   print(f"Hi {uName} Because U R From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")



# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

# country = "canda"

# if country == "Egypt" : print(f"The Weather in {country} Is 15")
# elif country == "KSA" : print(f"The Weather in {country} Is 30")
# else : print("Country is Not in The List")

#  Short If

# movieRate = 18
# age = 15

# if age < movieRate :

#   print("Movie S Not Good 4U") # Condition If True

# else :

#   print("Movie S Good 4U And Happy Watching") # Condition If False

# print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False



# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
# print("#" * 80)
# print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
# print("#" * 80)

# Collect Age Data
age = input("Please Write Your Age").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365
22
if unit == 'months' or unit == 'm':

  print("You Choosed The Unit Months")
  print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

  print("You Choosed The Unit Weeks")
  print(f"You Lived For {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

  print("You Choosed The Unit Days")
  print(f"You Lived For {days:,} Days.")
