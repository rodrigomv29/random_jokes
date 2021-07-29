import random_jokes
import db_jokes

isDone = false
name = input("Hello... What is your name?")
print("Hello " + name)
print("Would you like to hear a joke?")
yesOrNo = input ("Y/N? (Press N to quit or 1 for more options) ")
while(yesOrNo == "Y"):
  random_jokes = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  json_data = json.loads(random_jokes.content)
  joke = json_data["joke"]
  print(joke)
  print("\n\n")
  print("Would you like to hear another joke? ")
  yesOrNo = input ("Y/N? (Press N to quit or 1 for more options) ")

while(yesOrNo == "1"):
   print("1. Give me a joke with my conditions\n2. Data about joke library\n3. Submit a new joke\n4. Quit")
   numberInp = input("Choose one of the following? ")
  
if yesOrNo == "N":
   print("bye...")
   isDone=true
   db_jokes.closeConnection()

