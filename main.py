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
        artist_list.append(dict(name = artist_name, songs = artist_songs, performance_time = artist_performance_duration))
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