from tkinter import *
import time

while True:
 print("Would you like to play?") #START SCREEN#
 answer = input("Yes or No\n").lower().strip()

 if answer == "yes":
  print("Welcome to Norway. I am Oslinia, and I will serve as your guide.")
  Adventurer_name = input("To begin, what is your name adventurer?\n") #ASSIGNING A CHARACTER NAME

  while len(Adventurer_name) > 6:
        print("Name is limited to only 6 characters. Please try again.\n")
        Adventurer_name = input().lower().strip()

  while True:
   print(Adventurer_name + ". It is your 18th birthday and you are presented with either an axe or a pitchfork. Which do you choose?")
   answer = input("Axe or Pitchfork?\n").lower().strip()
   if answer == "axe":
        
         print("You receive an axe from your village. Three men approach you and ask you to go raiding with them.")
         answer = input("Agree or Disagree?\n").lower().strip()
         if answer == "agree":
                
                 print("You take to the seas and eventually stumble upon a coastal village.")
                 answer = input("Attack or Scout?\n").lower().strip()
                 if answer == "attack":
                        
                         print("A small garrison is located inside the town. You lose two men and only you and one other remain.")
                         answer = input("Flee or Continue?\n").lower().strip()
                         if answer == "flee":
                
                                print("Your companion chastises you for cowardice and carves your skull in with an axe")
                                print("YOU LOSE") #END OF A PLOT LINE#
                                time.sleep(3)
                                quit
                         elif answer == "continue":
                                print("The garrison chases you down and ultimately hangs you and your companion for the attack")
                                print("YOU LOSE\n") #END OF A PLOT LINE#
                                time.sleep(3)
                                quit
                         else:
                                print("Invalid choice. Please try again.\n")
                                answer = input().lower().strip()
                                
                         break
                                
                 elif answer == "scout":
                        print("You and your men see a garrison defending the town. When should you strike?")
                        answer = input("Day or Night?\n").lower().strip()
                        if answer == "day":
                                print("The garrison quickly overpowers you and you die")
                                print("YOU LOSE\n") #END OF A PLOT LINE#
                                time.sleep(3)
                                quit
                        elif answer == "night":
                                print("You and your men slip in under the cover of darkness.")
                                print("You kill the garrison without being detected")
                                print("You burn the city and steal the treasure")
                                print("Do you return home with treasure or continue the raid?")
                                answer = input("Home or Continue?\n").lower().strip()
                                if answer == "home":
                                                print("You return home with your spoils in tow and retire to a life of comfort")
                                                print("YOU WIN") #END OF A PLOT LINE#
                                                time.sleep(3)
                                                quit
                                elif answer == "Continue":
                                                print("Two of the men have murdered the third in a bid to claim his gold.")
                                                print("Do you fight them or take your gold and run?")
                                                answer = input("Fight or Run?\n").lower().strip()
                                                if answer == "fight":
                                                        print("You are quickly overpowered and your gold is seized by the other two.")
                                                        print("YOU LOSE") #END OF A PLOT LINE#
                                                        time.sleep(3)
                                                        quit
                                                elif answer == "run":
                                                        print("You outrun the other two men")
                                                        print("You hide in a barn for the night")
                                                        print("A man comes out saying he heard someone come in. Do you reveal yourself or stay hidden?")
                                                        answer = input("Reveal or Hide\n").lower().strip()
                                                        if answer == "reveal":
                                                                print("The man asks if you are willing to take gold and leave.")
                                                                answer = input("Accept or Decline").lower().strip()
                                                                if answer == "accept":
                                                                        print("You take the gold and return home with the wealth you accumulated.")
                                                                        print("YOU WIN") #END OF A PLOT LINE#
                                                                        time.sleep(3)
                                                                        quit
                                                                elif answer == "decline":
                                                                        print("The farmer shouts for his family. His three sons come out and the four overpower and kill you.")
                                                                        print("YOU LOSE") #END OF A PLOT LINE#
                                                                        time.sleep(3)
                                                                        quit
                                                                else:
                                                                        print("Invalid choice. Please try again.\n")
                                                                        answer = input().lower().strip()
                                                                        continue
                                                                break
                                                        elif answer == "hide":
                                                                print("The farmer, not willing to put his family at risk, sets fire to the barn and kills you inside")
                                                                print("YOU LOSE") #END OF A PLOT LINE#
                                                                time.sleep(3)
                                                                quit
                                                        else:
                                                                print("Invalid choice. Please try again.\n")
                                                                answer = input().lower().strip()
                                                                continue
                                                        break
                                                else:
                                                        print("Invalid choice. Please try again.\n")
                                                        answer = input().lower().strip()
                                                        continue
                                                break
                                else:
                                 print("Invalid choice. Please try again.\n")
                                 answer = input().lower().strip()
                                 continue
                                break 
                        else:
                         print("Invalid choice. Please try again.\n")
                         answer = input().lower().strip()
                         continue
                        break   
                                                
         elif answer == "disagree": 
                print("The men decide to kill you and take your equipment.")
                print("YOU LOSE") #END OF A PLOT LINE#
                time.sleep(3)
                quit
         else:
          print("Invalid choice. Please try again.\n")
          answer = input().lower().strip()
          continue
         break 
   elif answer == "pitchfork":
        print("A simple life you attempt to lead. Tending crops and starting a family. Raiders threaten this peace and attempt to raid your village. (Fight OR Flee)\n")
        if answer == ("fight"):
                print("The raiders quickly overpower you and murder your entire village")
                print("YOU LOSE") #END OF A PLOT LINE#
                time.sleep(3)
                quit
        elif answer == "flee":
                print("An arrow pierces your back as you attempt to escape")
                print("YOU LOSE") #END OF A PLOT LINE#
                time.sleep(3)
                quit
        else:
          print("Invalid choice. Please try again.\n")
          answer = input().lower().strip()
          continue
        break 
   else:
    print("Invalid choice. Please try again.\n")
    answer = input().lower().strip()
 elif answer == "no":
  print("Okay. Thank you!")
  time.sleep(3)
  quit 