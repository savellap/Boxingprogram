

def search():
    print("Search Name")
    outcome = input("Enter keyword, or type etc:")
    print(":\nName #1 \nName #2\nName #3")
    print("\n")




def event_list():
    list = ["Event 1","Event 2","Event 3"]
    print("Upcoming Events:", list)
    print("\n")


def search_social_media():
    print("Search Name")
    outcome = input("Enter keyword, or type etc:")
    print(":\nName #1 \nName #2\nName #3")
    print("\n")

def advanced_options():
    print("coming soon!")
    print("\n")


def exit_program():
    quit()




print("Boxing Lite!")
print("\n")
while True:
    print("Please Enter a Number to select an action")

    print("1. Search a Boxer's Profile")
    print("2. Upcoming Events")
    print("3. Social Media of Boxer")
    print("4. Updates to the program")
    print("5. Exit")

    choice = input("Enter your number here ")
    print("\n")

    if choice == "1":
        search()

    if choice == "2":
        event_list()

    if choice == "3":
        search_social_media()

    if choice == "4":
        advanced_options()

    if choice == "5":
        exit_program()

