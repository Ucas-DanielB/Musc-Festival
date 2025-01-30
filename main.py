
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

# Avery music festival

from datetime import datetime, timedelta

# List of artists name and Genre
artists = [
    ("Artist 1", "Rock"),
    ("Artist 2", "Pop"),
    ("Artist 3", "Hip-Hop"),
    ("Artist 4", "Jazz"),
    ("Artist 5", "EDM"),
    ("Artist 6", "Country"),
    ("Artist 7", "Indie"),
    ("Artist 8", "Metal"),
    ("Artist 9", "Classical"),
    ("Artist 10", "Folk"),
    ("Artist 11", "Reggae"),
    ("Artist 12", "Blues"),
    ("Artist 13", "Rock"),
    ("Artist 14", "Pop"),
    ("Artist 15", "Hip-Hop"),
    ("Artist 16", "Jazz"),
    ("Artist 17", "EDM"),
    ("Artist 18", "Country"),
    ("Artist 19", "Indie"),
    ("Artist 20", "Metal"), 
    ("Artist 21", "Classical"),
    ("Artist 22", "Folk"),
    ("Artist 23", "Reggae"),
    ("Artist 24", "Blues"),
    ("Artist 25", "Rock"),
    ("Artist 26", "Pop"),
    ("Artist 27", "Hip-Hop"),
    ("Artist 28", "Jazz"),
    ("Artist 29", "EDM"),
    ("Artist 30", "Country"),
    ("Artist 31", "Indie"),
    ("Artist 32", "Metal"),
    ("Artist 33", "Classical"),
    ("Artist 34", "Folk"),
    ("Artist 35", "Reggae"),
    ("Artist 36", "Blues"),
]

# Festival details
days = ["Day 1", "Day 2", "Day 3"]
venues = ["Main Stage", "Second Stage"]
start_time = datetime.strptime("10:00 AM", "%I:%M %p")
end_time = datetime.strptime("10:00 PM", "%I:%M %p")
slot_duration = timedelta(hours=2)

# Function to create the schedule
def create_schedule():
    schedule = []
    artist_index = 0

    for day in days:
        current_time = start_time

        while current_time < end_time:
            for venue in venues:
                if artist_index < len(artists):
                    artist, genre = artists[artist_index]
                    end_slot = current_time + slot_duration
                    schedule.append((day, current_time.strftime("%I:%M %p"), 
                                     end_slot.strftime("%I:%M %p"), venue, artist, genre))
                    artist_index += 1
                current_time += slot_duration
    return schedule

# Generate schedule
festival_schedule = create_schedule()

# Display schedule
print(f"{'Day':<10} {'Start Time':<10} {'End Time':<10} {'Venue':<15} {'Artist':<15} {'Genre'}")
print("-" * 80)
for entry in festival_schedule:
    print(f"{entry[0]:<10} {entry[1]:<10} {entry[2]:<10} {entry[3]:<15} {entry[4]:<15} {entry[5]}")




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

def artist_lineup(artist_list, time_slots):
    pass
