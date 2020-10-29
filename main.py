print("This is my shopping list programme")

file = open ("shopping.txt", "a")

decision = input("What would you like to do? \nAdd something new to the list(add)\nChange something in the list(change)\nView the content inside the file(view)\nRemove something from the list(Remove)\nEnter answer here:")

if decision == "add":
  food = input("What do you wanna buy?")
  price = input("How much is it?")
  quantity = input("How much do you want?")

  file.write("Item name:" + food)
  file.write("\nPrice:£" + price)
  file.write("\nquantity:"+ quantity)
  file.write("\n____________\n")

elif decision == "view":
  file = open ("shopping.txt" , "r+")
print("")
for x in file:
    print (x)

if decision == "remove":

  removeall = input("Do you want delete all the content inside the shopping list?")
  if removeall == "yes" or removeall == "Yes":
    file.turncate()

  else:
   f = open ("shopping.txt" , "r")
  print("")
  for x in f:
      print (x)

  file = open("shopping.txt", "r")


lines = file.readlines()
file.close()

item = int(input("What number item do you want to delete?\nEnter answer here:"))
if item == 1:
  number1 = 0
  number2 = 1
  number3 = 2
  number4 = 3
else:
  number1 = (1*item)-1
  number2 = 


del lines[0]


file = open("shopping.txt", "w+")

for line in lines:
    file.write(line)

file.close()
   

file.close()