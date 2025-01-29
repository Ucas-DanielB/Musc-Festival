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