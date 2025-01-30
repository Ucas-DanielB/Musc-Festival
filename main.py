
# Daniel code :D 

# Ticket and Attendee Management System for a Music Festival

# Ticket storage and attendees
bought_tickets = {"1-day": 0, "3-day": 0, "vip": 0}
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

=======
#Max Holdaway, Daniel Blanco, Avery Bowman, Aiden Challenger :D

#Max's Section
import random

list_of_artist_venue_1 = []
list_of_artist_venue_2 = []
artist_lineup = []

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

def search_for_artist(artist_name, artist_list):
    for index, artist_record in enumerate(artist_list):
        if artist_record["name"] == artist_name:
            return index

def add_artists(artist_list, artist_name, artist_songs, artist_performance_duration):
    if search_for_artist(artist_name, artist_list) is None:
        artist_list.append(dict(name = artist_name, songs = artist_songs, performance_duration = artist_performance_duration))
        print("You have successfully added the artist to the list.")
    else:
        print("The artist is already inside the list")
    return artist_list

def remove_artist(artist_list, artist_name):
    index = search_for_artist(artist_list, artist_name)
    if index is not None:
        artist_list.pop(index)
        print("You have succesfully removed the artist from the list.")
    else:
        print("The artist you are trying to remove does not exist.")

def update_artist_info(artist_list, artist_name, artist_songs=None, artist_performance_duration=None):
    index = search_for_artist(artist_list, artist_name)
    if index is not None:
        artist_record = artist_list[index]
        if artist_songs is not None:
            artist_record["songs"] = artist_songs
        if artist_performance_duration is not None:
            artist_record["performance_time"] = artist_performance_duration
    elif index is None:
        print("The artist you were trying to update does not exist.")
    return artist_list



# Avery music festival

from datetime import datetime, timedelta


# List of 36 artists with genres
list_of_artist_venue_1 = []
list_of_artist_venue_2 = []


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
   unscheduled = [artist for artist in artists if artist[0] not in scheduled_artists]


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
       if len(venues["Venue 1"]) + len(venues["Venue 2"]) == len(artists):
           print("\nAll artists have been scheduled!")
           return False


   return True


# Scheduling process
while len(venues["Venue 1"]) + len(venues["Venue 2"]) < len(artists):
   if not schedule_artist():
       break  # Exit loop if user quits


# Display final schedule
print("\nFinal Festival Schedule:")
print(f"{'Day':<10} {'Time':<10} {'Venue':<10} {'Artist':<15} {'Genre'}")
print("-" * 60)
for venue in venues:
   for day, time, (artist, genre) in sorted(venues[venue], key=lambda x: (days.index(x[0]), x[1])):
       print(f"{day:<10} {time.strftime('%I:%M %p'):<10} {venue:<10} {artist:<15} {genre}")



def artist_lineup(artist_list, time_slots):
    pass
