# program for going in fair
height=int(input("what is your height" ))
bill=0
if height>=3:
  print("can ride")
age=int(input("what is your age?"))
if age<12:
  bill=150
  print("ticket price is 150rs")
elif age<=18:
  bill=250
  print("ticket price is 250rs")
else:
  bill=500
  print("ticket price is 500rs")
want_photo=input("do you want to take a photo(y/n)?")
if want_photo=='y'or want_photo=='Y':
    bill=bill + 50
    print(f"you total bill is{bill}")
else:
    print("cant ride")
    print("bye")
