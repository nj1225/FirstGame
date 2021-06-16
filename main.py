print("Welcome to my CHOICE game,HOPE YOU ENJOY IT")

name=input("What is your name?")

age=int(input("What is your age?"))

print("Hello" , name, "your", age, "years old")

health = 10
print("you are starting with ", health , "health")

if age >= 18:
  print("you are old enough to play")

  weapon = input("pick a weapon (sword/ baton)")

  if weapon == "sword":
    print("you got 2 extra health") 
    health += 2
  else:
    print("you got 1 extra health ") 
    health += 1 

  print("cureent health ", health)  

  wants_to_play = input("do you want to play????").lower()
  if wants_to_play == "yes":
    print("let's play!!!")
    left_or_right = input("first choice .... left or right (left/right)? ").lower()
    if left_or_right == "left":
      ans = input("nice ,you followed the path and reach a forest, do you pass across / go around(across/around)????").lower()
      if ans == "around":
        print ("you went around and reached the other side of the forest and got sting by a bee .Lost 2 health")
        health -= 2 

        



      elif ans == "across":
        print("you managed to get across ,  but were bit by a tiger and lost 5 health")
        health -= 5


      ans = input("YOU notice a house and a river,which do you go to(river/house)???") 
      if ans == "house":
        print("go to the house and greted by the owner...he does not like you and attacked you for that you losed 5 health")

        health -=5
        if health <= 0:
          print("you now have 0 health and you lose the game.... ")
        else:
            print("you survived and win ,also move to the next level...") 

      else: 
        print("you fell down and bitten by a croc lost 6 health .....")
        health -= 6
        if health <= 0:
          print("you now have 0 health and you lose the game.... ")
        else:
            print("you survived and win ,also move to the next level...")  



    else:
      print("you fell down the clif and lost.START AGAIN....")   

  else:
    print("EXIT THE GAME...")  

elif age >= 14:
  print ("you can play with supervision") 
else:
  print("you are not old enough")
