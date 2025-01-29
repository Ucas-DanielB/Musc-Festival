# :D
#Aiden Challenger UI/UX Venue Mangment for Music Festival


#define sets for venue mangment
#not all need to be sets 
venue_names = {}
stage_names = {}  #job 1  hit up avery

artist_name= () #take infor from job 1

equipment_names={} 


#defining future functions 
def add_things(): #get better naming skills idiot
  venue_names
  
  #assign location to venue
  


def equipment():
  

  #view venue function 
  def view_venue(): #please take info and ask for vari names
    #take info from job one 
    #ask user what venue they want to choose

#edit venue function 
def edit_venue():
  print("1. add to venue")#DUMB WHAT DOES ADD ENTAIL
  print("2. Remove from venue")#same thing
  print("3. 
  edit_choice =int(input("what do you want to do")




#venue function(display) 
def venue_menu():
  print("please pick something")
  print("1. view venues") #display with schedules for each venue 
  print("2. edit venues")#admin only
  print("3. Equipment lists")#prob admin only
  print("4. return") 
  #yn's have ought to add something but they forgor
  venue_choice=int(input("what do you wish to use"))
  if venue_choice== 1:
      view_venue()
      pass
  if venue_choice== 2:
      edit_venue()
      pass
  if venue_choice== 3:
    equipment()
    pass
  if venue_choice== 4:
    continue



 
  














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
    choice= int(input("What do you want to use (1-5: )"))
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
