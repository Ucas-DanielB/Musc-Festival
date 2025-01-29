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
