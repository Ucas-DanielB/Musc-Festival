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