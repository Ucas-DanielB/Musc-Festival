# :D
#Aiden Challenger UI/UX Venue Mangment for Music Festival


#define sets for venue mangment
#not all need to be sets 

venue_names = set()  
stage_info = {} {stage_name: location}
equipment_lists = {}  : {stage_name: set(equipment)}


#defining future functions 
def add_venue(): 
  venue=input("What would you like the new venue to be named: ").strip()
  #check if it exists already
  venue_names.append(venue)
  #won't work fix
  print(f'Added {venue_names}")
  

  #adding equipment
def add_equipment():
    stage = input("Enter stage name: ").strip()
    if stage not in stage_info:
        print("Stage does not exist. Add the stage first.")
        return
    equipment = input("Enter equipment name: ").strip()
    if stage not in equipment_lists:
        equipment_lists[stage] = set()
    equipment_lists[stage].add(equipment)
    print(f"Added {equipment} to {stage}.")

 
#adding stages
def add_stage():
    stage = input("Enter stage name: ").strip()
    location = input("Enter stage location: ").strip()
    if stage in stage_info:
        print("Stage already exists.")
    else:
        stage_info[stage] = location
        print(f"Added stage '{stage}' at '{location}'.")


  #view venue function 
  def view_venue(): #please take info and ask for vari names
     if not venue_names:
        print("No venues added yet.")
    else:
        print("Venues:")
        for venue in venue_names:
            print(f"- {venue}")


#edit venue function 
def edit_venue():
  view_venues()
  print("1. Rename venue")
  print("2. Remove venue")
  choice = input("Choose an option (1/2): ")
    
  if choice == "1":
     new_name = input("Enter new venue name: ").strip().lower()
     venue_names.remove(venue)
     venue_names.add(new_name)
       print(f"Venue renamed to {new_name}")
     elif choice == "2":
      venue_names.remove(venue)
        print(f"Venue '{venue}' removed.")

#venue function(display) 
def venue_menu():
  print("please pick something")
  print("1. view venues") #display with schedules for each venue 
  print("2. edit venues")#admin only
  print("3. Add stages")
  print("4. remove stages")
  print("5. Equipment lists")#prob admin only
  print("6. return") 
  venue_choice=int(input("what do you wish to use"))
  if venue_choice== 1:
      view_venue()
  if venue_choice== 2:
      edit_venue()
  if venue_choice== 3:
    add_stage()
  if venue_choice== 4:
    add_stage()
  if venue_choice== 5:
    add_equipment()
  if venue_choice== 6:
    return



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
    elif choice== 2:
      #place holder for schedule functions
      pass
    elif choice== 3:
      #placeholder for venue functions
      pass
    elif choice== 4:
      #placeholder for ticket function 
      pass
    elif choice== 5:
      break 

if __name__ == "__main__"
