# :D
#Aiden Challenger UI/UX Venue Mangment for Music Festival


#define sets for venue mangment


#venue function(display) 
def venue_menu():
  print("please pick something")
  print("1. view venues") 
  print("2. edit venues")#admin only
  print("3. Equipment lists")
  print("4. return") 
  
  
  














#main function 
#maybe add more depending on what other need  
def main(): 
  while True:
    print("Welcome to our music festival!")
    print("1. View venues ") #reorganize in order listed
    print("2. View Artists Perfoming")
    print("3. View Schedules")
    print("4. Buy Tickets")
    print("5. Exit")
    choice= int(input("What do you want to use (1-5)"))
#send user to function 
    if choice== 1:
      #placeholder for artist functions
      pass
    if choice== 2:
      #place holder for schedule functions
      pass
    if choice== 3:
      #placeholder for venue functions
      pass
    if choice== 4:
      #placeholder for ticket function 
      pass
    if choice== 5:
      break 

if __name__ == "__main__"
