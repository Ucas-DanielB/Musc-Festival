# :D
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
            
#max artist function (suggest adding way to directly show all artists) 
def artist_menu():
    while True:
        print("\nArtist Managment Menu:")
        print("1. Search for artists")
        print("2. Add artists(Admin only)")
        print("3. Remove artists(Admin only)")
        print("4. Update artist information(Admin only")
        print("5. Return to main menu")
        venue_choice = int(input("What do you wish to use (1-5): "))
        if venue_choice == 1:
            search_for_artist(artist_name, artist_list()
        elif venue_choice == 2:
            add_artists(artist_list, artist_name, artist_songs, artist_performance_duration)
        elif venue_choice == 3:
            remove_artist(artist_list, artist_name)
        elif venue_choice == 4:
            update_artist_info(artist_list, artist_name, artist_songs=None, artist_performance_duration=None)
        elif venue_choice == 5:
            return
        else:
            print("Invalid choice")
            
#daniel ticket function 
def tickets():
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
#start the function
if __name__ == "__main__":
    main()
