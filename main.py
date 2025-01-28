#Max Holdaway, Daniel Blanco, Avery Bowman, Aiden Challenger :D

#Max's Section
import random

Artist1 = dict(name = "", song = "", time = "", num = 1, in_use = False)
Artist2 = dict(name = "", song = "", time = "", num = 2, in_use = False)
Artist3 = dict(name = "", song = "", time = "", num = 3, in_use = False)
Artist4 = dict(name = "", song = "", time = "", num = 4, in_use = False)
Artist5 = dict(name = "", song = "", time = "", num = 5, in_use = False)
Artist6 = dict(name = "", song = "", time = "", num = 6, in_use = False)
Artist7 = dict(name = "", song = "", time = "", num = 7, in_use = False)
Artist8 = dict(name = "", song = "", time = "", num = 8, in_use = False)
Artist9 = dict(name = "", song = "", time = "", num = 9, in_use = False)
Artist10 = dict(name = "", song = "", time = "", num = 10, in_use = False)
Artist11 = dict(name = "", song = "", time = "", num = 11, in_use = False)
Artist12 = dict(name = "", song = "", time = "", num = 12, in_use = False)
Artist13 = dict(name = "", song = "", time = "", num = 13, in_use = False)
Artist14 = dict(name = "", song = "", time = "", num = 14, in_use = False)
Artist15 = dict(name = "", song = "", time = "", num = 15, in_use = False)
Artist16 = dict(name = "", song = "", time = "", num = 16, in_use = False)
Artist17 = dict(name = "", song = "", time = "", num = 17, in_use = False)
Artist18 = dict(name = "", song = "", time = "", num = 18, in_use = False)
Artist19 = dict(name = "", song = "", time = "", num = 19, in_use = False)
Artist20 = dict(name = "", song = "", time = "", num = 20, in_use = False)
Artist21 = dict(name = "", song = "", time = "", num = 21, in_use = False)
Artist22 = dict(name = "", song = "", time = "", num = 22, in_use = False)
Artist23 = dict(name = "", song = "", time = "", num = 23, in_use = False)
Artist24 = dict(name = "", song = "", time = "", num = 24, in_use = False)
Artist25 = dict(name = "", song = "", time = "", num = 25, in_use = False)
Artist26 = dict(name = "", song = "", time = "", num = 26, in_use = False)
Artist27 = dict(name = "", song = "", time = "", num = 27, in_use = False)
Artist28 = dict(name = "", song = "", time = "", num = 28, in_use = False)
Artist29 = dict(name = "", song = "", time = "", num = 29, in_use = False)
Artist30 = dict(name = "", song = "", time = "", num = 30, in_use = False)
Artist31 = dict(name = "", song = "", time = "", num = 31, in_use = False)
Artist32 = dict(name = "", song = "", time = "", num = 32, in_use = False)
Artist33 = dict(name = "", song = "", time = "", num = 33, in_use = False)
Artist34 = dict(name = "", song = "", time = "", num = 34, in_use = False)
Artist35 = dict(name = "", song = "", time = "", num = 35, in_use = False)
Artist36 = dict(name = "", song = "", time = "", num = 36, in_use = False)

list_of_artist = [Artist1, Artist2, Artist3, Artist4, Artist5, Artist6, Artist7, Artist8, Artist9, Artist10, Artist11, Artist12, Artist13, Artist14, Artist15, Artist16, Artist17, Artist18, Artist19, Artist20, Artist21, Artist22, Artist23, Artist24, Artist25, Artist26, Artist27, Artist28, Artist29, Artist30, Artist31, Artist32, Artist33, Artist34, Artist35, Artist36]

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
        
def add_remove_update(artist_list):
    user_admin_status = admin_checker()
    if user_admin_status == True:
        while True:
            user_decision = int(input("""Which option do you want to do?
                                      1. Add artist and information for artist
                                      2. Remove artist and information for said artist
                                      3. Update information for an artist
                                      4. Exit\n"""))
            if user_decision == 1:
                user_artist_selection = int(input("Select an open artist in the list (based on number): "))
                for x in artist_list:
                    if user_artist_selection in x:
                        print(x)

add_remove_update(list_of_artist)