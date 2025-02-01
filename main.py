#Music Festival
#Max Holdaway, Daniel Blanco, Avery Bowman, Aiden Challenger :D
#Aiden Challenger UI/UX Venue Mangment for Music Festival


#defining sets and dictonaries 
venue_names = {} 
stage_info = {}  
equipment_lists = {}  
artist_schedules = {}  

# adding venue 
def add_venue():
    if len(venue_names) >= 2:
        print("the maximum amount of venues is 2")
        return
    venue = input("What would you like the new venue to be named: ").strip()
    if venue in venue_names:
        print("Venue already exists")
    else:
        venue_names.add(venue)
        stage_info[venue] = {}
        equipment_lists[venue] = {}
        artist_schedules[venue] = {}
        print(f"Added {venue}")

# adding stage to venue
def add_stage():
    if not admin_checker():
        print("Admin access required")
        return
    if not venue_names:
        print("No venues added yet")
        return
    view_venue()
    venue = input("Enter the venue to add a stage to: ").strip()
    if venue not in venue_names:
        print("Venue does not exist")
        return
    stage = input("Enter stage name: ").strip()
    location = input("Enter stage location: ").strip()
    if stage in stage_info[venue]:
        print("Stage already exists")
    else:
        stage_info[venue][stage] = location
        equipment_lists[venue][stage] = set()
        artist_schedules[venue][stage] = {}
        print(f"Added stage '{stage}' at '{location}' in '{venue}'.")

# viewing venue  functions 
def view_venue():
    if not venue_names:
        print("No venues added yet.")
    else:
        print("Venues:")
        for venue in venue_names:
            print(f"- {venue}")
            print("  Stages:")
            for stage, location in stage_info[venue].items():
                print(f"  - {stage} at {location}")
                print("    Artists:")
                for artist, time in artist_schedules[venue][stage].items():
                    print(f"    - {artist} performing at {time}")

# venue editing (add/remove/rename)
def edit_venue():
    if not admin_checker():
        print("Admin access required")
        return
    while True:
        view_venue()
        print("\nEdit Venue Options:")
        print("1. Rename a venue")
        print("2. Remove a venue")
        print("3. Add a new venue")
        print("4. Return to venue menu")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            venue = input("Enter venue name to rename: ").strip()
            if venue not in venue_names:
                print("Venue does not exist")
                continue
            new_name = input("Enter new venue name: ").strip()
            if new_name in venue_names:
                print("venue name already exists")
                continue
            venue_names.remove(venue)
            venue_names.add(new_name)
            stage_info[new_name] = stage_info.pop(venue)
            equipment_lists[new_name] = equipment_lists.pop(venue)
            artist_schedules[new_name] = artist_schedules.pop(venue)
            print(f"Venue renamed to {new_name}")
        elif choice == "2":
            venue = input("Enter venue name to remove: ").strip()
            if venue not in venue_names:
                print("Venue does not exist")
                continue
            venue_names.remove(venue)
            del stage_info[venue]
            del equipment_lists[venue]
            del artist_schedules[venue]
            print(f"venue '{venue}' removed.")
        elif choice == "3":
            add_venue()
        elif choice == "4":
            return
        else:
            print("Invalid choice")

# adding equipment 
def add_equipment():
    if not admin_checker():
        print("Admin access required")
        return
    if not venue_names:
        print("No venues added yet")
        return
    view_venue()
    venue = input("Enter the venue: ").strip()
    if venue not in venue_names:
        print("Venue does not exist")
        return
    stage = input("Enter stage name: ").strip()
    if stage not in stage_info[venue]:
        print("Stage does not exist")
        return
    equipment = input("Enter equipment name: ").strip()
    equipment_lists[venue][stage].add(equipment)
    print(f"Added {equipment} to {stage} in {venue}.")

# viewing equipment lists
def view_equipment():
    if not admin_checker():
        print("Admin access required")
        return
    if not venue_names:
        print("No venues added yet")
        return
    view_venue()
    venue = input("Enter the venue: ").strip()
    if venue not in venue_names:
        print("Venue does not exist")
        return
    stage = input("Enter stage name: ").strip()
    if stage not in stage_info[venue]:
        print("Stage does not exist")
        return
    print(f"Equipment for {stage} in {venue}:")
    for equipment in equipment_lists[venue][stage]:
        print(f"- {equipment}")

# assigning artissts to diffrent days
def assign_artist():
    if not admin_checker():
        print("Admin access required.")
        return
    view_venue()
    venue = input("Enter the venue: ").strip()
    if venue not in venue_names:
        print("Venue does not exist.")
        return
    stage = input("Enter stage name: ").strip()
    if stage not in stage_info[venue]:
        print("Stage does not exist.")
        return
    artist = input("Enter artist name: ").strip()
    day = input("Enter day (Day 1, Day 2, Day 3): ").strip()
    time = input("Enter time (e.g., 10:00 AM): ").strip()
    
    if day not in ["Day 1", "Day 2", "Day 3"]:
        print("Invalid day.")
        return
    try:
        datetime.strptime(time, "%I:%M %p")
    except ValueError:
        print("Invalid time format try something like this (10:00AM) ")
        return
    artist_schedules[venue][stage][artist] = f"{day} at {time}"
    print(f"Assigned {artist} to {stage} in {venue} on {day} at {time}.")

# Venue menu function(aiden)
def venue_menu():
    while True:
        print("\nVenue Management Menu:")
        print("1. View venues")
        print("2. Edit venues (Admin only)")
        print("3. Add stages (Admin only)")
        print("4. Add equipment (Admin only)")
        print("5. View equipment lists (Admin only)")
        print("6. Assign artists to slots (Admin only)")
        print("7. Return to main menu")
        venue_choice = int(input("What do you wish to use (1-7): "))
        if venue_choice == 1:
            view_venue()
        elif venue_choice == 2:
            edit_venue()
        elif venue_choice == 3:
            add_stage()
        elif venue_choice == 4:
            add_equipment()
        elif venue_choice == 5:
            view_equipment()
        elif venue_choice == 6:
            assign_artist()
        elif venue_choice == 7:
            return
        else:
            print("Invalid choice")

# main function/ menu selection 
def main():
    while True:
        print("\nWelcome to our music festival!")
        print("1. Open venue menu")
        print("2. View artist menu")
        print("3. View schedule menu")
        print("4. Buy Tickets")
        print("5. Exit")
        choice = int(input("What do you want to use (1-5): "))
        if choice == 1:
            venue_menu()
        elif choice == 2:
            artist_menu()
        elif choice == 3:
            schedule_menu()
        elif choice == 4:
            tickets()
        elif choice== 5:
            break
        else:
            print("Invalid choice")


#menu for schedule (Avery)
def schedule_menu():
    while True:
        print("\nSchedule Managment Menu:")
        print("1. View final schedule")
        print("2. Schedule an artist(Admin only)")
        print("3. Return to main menu")
        venue_choice = int(input("What do you wish to use (1-3): "))
        if venue_choice == 1:
            print("\nFinal Festival Schedule:")
            print(f"{'Day':<10} {'Time':<10} {'Venue':<10} {'Artist':<15} {'Genre'}")
            print("-" * 60)
            for venue in venues:
                for day, time, (artist, genre) in sorted(venues[venue], key=lambda x: (days.index(x[0]), x[1])):
                    print(f"{day:<10} {time.strftime('%I:%M %p'):<10} {venue:<10} {artist:<15} {genre}")
        elif venue_choice == 2:
            schedule_artist()
        elif venue_choice == 3:
            return
        else:
            print("Invalid choice")\

# Daniel code :D 
# Ticket and Attendee Management System for a Music Festival

# Ticket storage and attendees
def tickets():
bought_tikets = {"1-day": 0, "3-day": 0, "vip": 0}
unbought_tickets = {"1-day": 200, "3-day": 100, "vip": 40}
attendees = {"people attending total": 340}

# Function to display available tickets
def display_tickets():
    print("\nAvailable Tickets:")
    for ticket_type, count in unbought_tickets.items():
        print(f"{ticket_type.capitalize()} Tickets: {count}")
    
    print("\nBought Tickets:")
    for ticket_type, count in bought_tickets.items():
        print(f"{ticket_type.capitalize()} Tickets: {count}")
    print(f"{attendees}")

# Function to buy tickets
def buy_ticket():
    ticket_type = input("Enter ticket type (1-day, 3-day, vip): ").strip().lower()
    
    if ticket_type not in unbought_tickets:
        print("\nInvalid ticket type.")
        return

    try:
        quantity = int(input("Enter number of tickets: "))
        if quantity <= 0:
            print("\nInvalid quantity.")
            return

        if unbought_tickets[ticket_type] >= quantity:
            unbought_tickets[ticket_type] -= quantity
            bought_tickets[ticket_type] += quantity
            print(f"\nSuccessfully bought {quantity} {ticket_type} tickets.")
        else:
            print("\nNot enough tickets available.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Function to refund tickets
def refund_ticket():
    display_tickets()
    ticket_type = input("Enter ticket type to refund: ").strip().lower()
    
    if ticket_type not in bought_tickets or bought_tickets[ticket_type] == 0:
        print("\nYou have no tickets of this type to refund.")
        return

    try:
        quantity = int(input("Enter number of tickets to refund: "))
        if quantity <= 0 or bought_tickets[ticket_type] < quantity:
            print("\nRefund failed: Insufficient tickets.")
            return

        bought_tickets[ticket_type] -= quantity
        unbought_tickets[ticket_type] += quantity
        print(f"\nSuccessfully refunded {quantity} {ticket_type} tickets.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Function to upgrade tickets
def upgrade_ticket():
    display_tickets()
    old_ticket = input("Enter current ticket type: ").strip().lower()
    new_ticket = input("Enter ticket type to upgrade to: ").strip().lower()

    if old_ticket not in bought_tickets or bought_tickets[old_ticket] == 0:
        print("\nYou have no tickets of this type to upgrade.")
        return

    if new_ticket not in unbought_tickets:
        print("\nInvalid ticket type.")
        return

    try:
        quantity = int(input("Enter number of tickets to upgrade: "))
        if quantity <= 0 or bought_tickets[old_ticket] < quantity:
            print("\nUpgrade failed: Insufficient tickets.")
            return

        if unbought_tickets[new_ticket] < quantity:
            print("\nUpgrade failed: Not enough new ticket type available.")
            return

        bought_tickets[old_ticket] -= quantity
        unbought_tickets[old_ticket] += quantity
        unbought_tickets[new_ticket] -= quantity
        bought_tickets[new_ticket] += quantity
        print(f"\nSuccessfully upgraded {quantity} {old_ticket} tickets to {new_ticket} tickets.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

# Main function
def main():

    while True:
        print("\n1. View Tickets\n2. Buy Ticket\n3. Refund Ticket\n4. Upgrade Ticket\n5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_tickets()
        elif choice == "2":
            buy_ticket()
        elif choice == "3":
            refund_ticket()
        elif choice == "4":
            upgrade_ticket()
        elif choice == "5":
            print("\nExiting ticket system.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

#Max's Section
import random

#Getting all the lists for the artists in venues 1 and 2 as well as the artist lineup
list_of_artists = []
artist_lineup = []
list_of_artist_for_scheduler = []


#Function for checking if user is an admin
def admin_checker():
    admin_status = False
    while True:
        user_decision = str(input("Do you want to try to login to admin or exit? (type admin for login, and exit for exiting): "))
        if user_decision.lower() == "admin":
            password_checker = str(input("Please enter password for admin: "))
            if password_checker == "Placeholder":
                print("That is the correct password welcome admin.")
                admin_status = True
                return admin_status
            else:
                print("That is the wrong password please try again.")
                admin_status = False
                return admin_status
        
        elif user_decision.lower() == "exit":
            print("Admin login is exiting.")
            return admin_status

#Function for searching for an artist
def search_for_artist(artist_name, artist_list):
    for index, artist_record in enumerate(artist_list):
        if artist_record["name"] == artist_name:
            return index

#Function for adding an artist with all their information
def add_artists(artist_list, artist_name, artist_genre, artist_performance_duration):
    if search_for_artist(artist_name, artist_list) is None:
        artist_list.append(dict(name = artist_name, genre = artist_genre, performance_duration = artist_performance_duration))
        print("You have successfully added the artist to the list.")
    else:
        print("The artist is already inside the list")
    return artist_list

#Function for removing artists
def remove_artist(artist_list, artist_name):
    index = search_for_artist(artist_list, artist_name)
    if index is not None:
        artist_list.pop(index)
        print("You have succesfully removed the artist from the list.")
    else:
        print("The artist you are trying to remove does not exist.")

#Function for updating artist information
def update_artist_info(artist_list, artist_name, artist_genre=None, artist_performance_duration=None):
    index = search_for_artist(artist_list, artist_name)
    if index is not None:
        artist_record = artist_list[index]
        if artist_genre is not None:
            artist_record["genre"] = artist_genre
        if artist_performance_duration is not None:
            artist_record["performance_time"] = artist_performance_duration
    elif index is None:
        print("The artist you were trying to update does not exist.")
    return artist_list

#Function for taking information from my artist list and making it into a list that the scheduler can use
def take_artist_info(list_of_artists, list_of_artists_schedule):
    for artist_record in list_of_artists:
        list_of_artists_schedule.append(artist_record["name"])
        list_of_artists_schedule.append(artist_record["genre"])
        return list_of_artists_schedule

# Avery music festival

from datetime import datetime, timedelta

# List of 36 artists
list_of_artist_for_scheduler = take_artist_info(list_of_artists, list_of_artist_for_scheduler)

# Festival details
days = ["Day 1", "Day 2", "Day 3"]
venues = {"Venue 1": [], "Venue 2": []}  # Empty schedule for both venues


# Time slots from 10:00 AM to 10:00 PM (2-hour slots)
start_time = datetime.strptime("10:00 AM", "%I:%M %p")
slot_duration = timedelta(hours=2)
time_slots = [start_time + slot_duration * i for i in range(6)]  # 6 slots per day


# Function to check available slots for a venue on a specific day
def available_slots(day, venue):
   scheduled_times = {slot for d, slot, _ in venues[venue] if d == day}
   return [slot.strftime("%I:%M %p") for slot in time_slots if slot not in scheduled_times]


# Function to display unscheduled artists
def display_unscheduled_artists():
   scheduled_artists = {artist for venue in venues.values() for _, _, (artist, _) in venue}
   unscheduled = [artist for artist in list_of_artist_for_scheduler if artist[0] not in scheduled_artists]


   if not unscheduled:
       print("All artists have been scheduled!")
       return None
  
   print("\nAvailable Artists:")
   for i, (artist, genre) in enumerate(unscheduled, 1):
       print(f"{i}. {artist} ({genre})")
  
   return unscheduled


# Function to schedule an artist
def schedule_artist():
   while True:
       print("\nAvailable time slots:")
       for day in days:
           for venue in venues:
               slots = available_slots(day, venue)
               if slots:
                   print(f"{day} - {venue}: {', '.join(slots)}")


       # Display unscheduled artists
       unscheduled = display_unscheduled_artists()
       if not unscheduled:
           break


       # Select an artist for the time they play
       artist_choice = input("Select an artist by number (or type 'exit' to quit): ").strip()
       if artist_choice.lower() == "exit":
           return False  # Exit scheduling


       try:
           artist_choice = int(artist_choice) - 1
           if artist_choice < 0 or artist_choice >= len(unscheduled):
               print("Invalid choice. Try again.")
               continue
           artist, genre = unscheduled[artist_choice]
       except ValueError:
           print("Enter a valid number.")
           continue


       # Select day 1, day 2, day 3 for the assigned day to the artist
       day = input("Enter the day (Day 1, Day 2, Day 3) or type 'exit' to quit: ").strip()
       if day.lower() == "exit":
           return False
       if day not in days:
           print("Invalid day. Try again.")
           continue


       # Select venue_1 or venue_2 for an artist
       venue = input("Enter the venue (Venue 1 or Venue 2) or type 'exit' to quit: ").strip()
       if venue.lower() == "exit":
           return False
       if venue not in venues:
           print("Invalid venue. Try again.")
           continue


       # Select a time slot for the artist
       slot_input = input("Enter the time slot (e.g., 10:00 AM) or type 'exit' to quit: ").strip()
       if slot_input.lower() == "exit":
           return False


       try:
           slot_time = datetime.strptime(slot_input, "%I:%M %p")
       except ValueError:
           print("Invalid time format. Use HH:MM AM/PM format.")
           continue


       if slot_time not in time_slots:
           print("Invalid time slot. Choose from the available slots.")
           continue


       if any(d == day and t == slot_time for d, t, _ in venues[venue]):
           print("Time slot already taken. Choose another one.")
           continue


       # If all checks pass, schedule the artist
       venues[venue].append((day, slot_time, (artist, genre)))
       print(f"Scheduled {artist} ({genre}) on {day} at {slot_time.strftime('%I:%M %p')} in {venue}.")
      
       # Stop scheduling when all artists are assigned
       if len(venues["Venue 1"]) + len(venues["Venue 2"]) == len(list_of_artist_for_scheduler):
           print("\nAll artists have been scheduled!")
           return False


   return True


# Scheduling process
while len(venues["Venue 1"]) + len(venues["Venue 2"]) < len(list_of_artist_for_scheduler):
   if not schedule_artist():
       break  # Exit loop if user quits


# Display final schedule
print("\nFinal Festival Schedule:")
print(f"{'Day':<10} {'Time':<10} {'Venue':<10} {'Artist':<15} {'Genre'}")
print("-" * 60)
for venue in venues:
   for day, time, (artist, genre) in sorted(venues[venue], key=lambda x: (days.index(x[0]), x[1])):
       print(f"{day:<10} {time.strftime('%I:%M %p'):<10} {venue:<10} {artist:<15} {genre}")


#(Part of Max's Section) Function for making artist lineup
def artist_lineup(artist_lineup):
    #Printing schedule to use for lineup
    print("\nFinal Festival Schedule:")
    print(f"{'Day':<10} {'Time':<10} {'Venue':<10} {'Artist':<15} {'Genre'}")
    print("-" * 60)
    for venue in venues:
        for day, time, (artist, genre) in sorted(venues[venue], key=lambda x: (days.index(x[0]), x[1])):
            print(f"{day:<10} {time.strftime('%I:%M %p'):<10} {venue:<10} {artist:<15} {genre}")
    
    #Giving clarifications to the user for making lineup
    print("The starting time is 10:00 AM and the ending time is 10:00 PM.")
    print("If there is not an artist in a specific time slot put TBD.")

    #Getting artists in lineup for first three days in venue 1
    first_artist_day_1_venue_1 = str(input("Who is the artist going first on day one, venue 1?: "))
    first_artist_day_2_venue_1 = str(input("Who is the artist going first on day two, venue 1?: "))
    first_artist_day_3_venue_1 = str(input("Who is the artist going first on day three, venue 1?: "))
    second_artist_day_1_venue_1 = str(input("Who is the artist going second on day one, venue 1?: "))
    second_artist_day_2_venue_1 = str(input("Who is the artist going second on day two, venue 1?: "))
    second_artist_day_3_venue_1 = str(input("Who is the artist going second on day three, venue 1?: "))
    third_artist_day_1_venue_1 = str(input("Who is the artist going third on day one, venue 1?: "))
    third_artist_day_2_venue_1 = str(input("Who is the artist going third on day two, venue 1?: "))
    third_artist_day_3_venue_1 = str(input("Who is the artist going third on day three, venue 1?: "))
    fourth_artist_day_1_venue_1 = str(input("Who is the artist going fourth on day one, venue 1?: "))
    fourth_artist_day_2_venue_1 = str(input("Who is the artist going fourth on day two, venue 1?: "))
    fourth_artist_day_3_venue_1 = str(input("Who is the artist going fourth on day three, venue 1?: "))
    fifth_artist_day_1_venue_1 = str(input("Who is the artist going fifth on day one, venue 1?: "))
    fifth_artist_day_2_venue_1 = str(input("Who is the artist going fifth on day two, venue 1?: "))
    fifth_artist_day_3_venue_1 = str(input("Who is the artist going fifth on day three, venue 1?: "))
    sixth_artist_day_1_venue_1 = str(input("Who is the artist going sixth on day one, venue 1?: "))
    sixth_artist_day_2_venue_1 = str(input("Who is the artist going sixth on day two, venue 1?: "))
    sixth_artist_day_3_venue_1 = str(input("Who is the artist going sixth on day three, venue 1?: "))

    #Getting artists in lineup for first three days in venue 2
    first_artist_day_1_venue_2 = str(input("Who is the artist going first on day one, venue 2?: "))
    first_artist_day_2_venue_2 = str(input("Who is the artist going first on day two, venue 2?: "))
    first_artist_day_3_venue_2 = str(input("Who is the artist going first on day three, venue 2?: "))
    second_artist_day_1_venue_2 = str(input("Who is the artist going second on day one, venue 2?: "))
    second_artist_day_2_venue_2 = str(input("Who is the artist going second on day two, venue 2?: "))
    second_artist_day_3_venue_2 = str(input("Who is the artist going second on day three, venue 2?: "))
    third_artist_day_1_venue_2 = str(input("Who is the artist going third on day one, venue 2?: "))
    third_artist_day_2_venue_2 = str(input("Who is the artist going third on day two, venue 2?: "))
    third_artist_day_3_venue_2 = str(input("Who is the artist going third on day three, venue 2?: "))
    fourth_artist_day_1_venue_2 = str(input("Who is the artist going fourth on day one, venue 2?: "))
    fourth_artist_day_2_venue_2 = str(input("Who is the artist going fourth on day two, venue 2?: "))
    fourth_artist_day_3_venue_2 = str(input("Who is the artist going fourth on day three, venue 2?: "))
    fifth_artist_day_1_venue_2 = str(input("Who is the artist going fifth on day one, venue 2?: "))
    fifth_artist_day_2_venue_2 = str(input("Who is the artist going fifth on day two, venue 2?: "))
    fifth_artist_day_3_venue_2 = str(input("Who is the artist going fifth on day three, venue 2?: "))
    sixth_artist_day_1_venue_2 = str(input("Who is the artist going sixth on day one, venue 2?: "))
    sixth_artist_day_2_venue_2 = str(input("Who is the artist going sixth on day two, venue 2?: "))
    sixth_artist_day_3_venue_2 = str(input("Who is the artist going sixth on day three, venue 2?: "))

    #Putting all the artists in a list to make the actual lineup
    artist_lineup = (f"{first_artist_day_1_venue_1} this is the first artist appearing on day one for venue 1\n", f"{second_artist_day_1_venue_1} this is the second artist appearing on day one for venue 1\n", f"{third_artist_day_1_venue_1} this is the third artist appearing on day one for venue 1\n", f"{fourth_artist_day_1_venue_1} this is the fourth artist appearing on day one for venue 1\n", f"{fifth_artist_day_1_venue_1} this is the fifth artist appearing on day one for venue 1\n", f"{sixth_artist_day_1_venue_1} this is the sixth/last artist appearing on day one for venue 1\n", f"{first_artist_day_2_venue_1} this is the first artist appearing on day two for venue 1\n", f"{second_artist_day_2_venue_1} this is the second artist appearing on day two for venue 1\n", f"{third_artist_day_2_venue_1} this is the third artist appearing on day two for venue 1\n", f"{fourth_artist_day_2_venue_1} this is the fourth artist appearing on day two for venue 1\n", f"{fifth_artist_day_2_venue_1} this is the fifth artist appearing on day two for venue 1\n", f"{sixth_artist_day_2_venue_1} this is the sixth/last artist appearing on day two for venue 1\n", f"{first_artist_day_3_venue_1} this is the first artist appearing on day three for venue 1\n", f"{second_artist_day_3_venue_1} this is the second artist appearing on day three for venue 1\n", f"{third_artist_day_3_venue_1} this is the third artist appearing on day three for venue 1\n", f"{fourth_artist_day_3_venue_1} this is the fourth artist appearing on day three for venue 1\n", f"{fifth_artist_day_3_venue_1} this is the fifth artist appearing on day three for venue 1\n", f"{sixth_artist_day_3_venue_1} this is the sixth/last artist appearing on day three for venue 1\n", f"{first_artist_day_1_venue_2} this is the first artist appearing on day one for venue 2\n", f"{second_artist_day_1_venue_2} this is the second artist appearing on day one for venue 2\n", f"{third_artist_day_1_venue_2} this is the third artist appearing on day one for venue 2\n", f"{fourth_artist_day_1_venue_2} this is the fourth artist appearing on day one for venue 2\n", f"{fifth_artist_day_1_venue_2} this is the fifth artist appearing on day one for venue 2\n", f"{sixth_artist_day_1_venue_2} this is the sixth/last artist appearing on day one for venue 2\n", f"{first_artist_day_2_venue_2} this is the first artist appearing on day two for venue 2\n", f"{second_artist_day_2_venue_2} this is the second artist appearing on day two for venue 2\n", f"{third_artist_day_2_venue_2} this is the third artist appearing on day two for venue 2\n", f"{fourth_artist_day_2_venue_2} this is the fourth artist appearing on day two for venue 2\n", f"{fifth_artist_day_2_venue_2} this is the fifth artist appearing on day two for venue 2\n", f"{sixth_artist_day_2_venue_2} this is the sixth/last artist appearing on day two for venue 2\n", f"{first_artist_day_3_venue_2} this is the first artist appearing on day three for venue 2\n", f"{second_artist_day_3_venue_2} this is the second artist appearing on day three for venue 2\n", f"{third_artist_day_3_venue_2} this is the third artist appearing on day three for venue 2\n", f"{fourth_artist_day_3_venue_2} this is the fourth artist appearing on day three for venue 2\n", f"{fifth_artist_day_3_venue_2} this is the fifth artist appearing on day three for venue 2\n", f"{sixth_artist_day_3_venue_2} this is the sixth/last artist appearing on day three for venue 2\n")
    return artist_lineup


