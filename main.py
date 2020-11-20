print("This is my shopping list programme")

def add():
  if decision == "add":
    file = open ("shopping.txt", "a")
    food = input("What do you wanna buy?")
    price = input("How much is it?")
    quantity = input("How much do you want?")

  file.write("Item name:" + food)
  file.write("\nPrice:£" + price)
  file.write("\nquantity:"+ quantity)
  file.write("\n____________\n")

def view():
  file = open ("shopping.txt" , "r")
  print("")
  for i in file:
     print (i)

def removeall():
  file = open ("shopping.txt" , "r")
  removeall = input("Do you want delete all the content inside the shopping list?")
  if removeall == "yes" or removeall == "Yes":
    file = open ("shopping.txt", "w")
    file.close()
  else:
    contents = file.readlines()
    file.close()
    c = 0
    choice = input("What item do you want to remove?")
    
    for lines in contents:
      if choice in lines:
        print(c)
        del contents[c]
        del contents[c]
        del contents [c]
        del contents [c]
      else:
        c+=1
      file.close()  
      file = open("shopping.txt", "w+")
      
      for lines in contents:
        file.write(lines)
      file.close()
decision = input("What would you like to do? \nAdd something new to the list(add)\nChange something in the list(change)\nView the content inside the file(view)\nRemove something from the list(Remove)\nEnter answer here:")
if decision.lower() == "add":
  add()

if decision.lower() == "view":
  view()

if decision.lower() == "remove":
  removeall()
