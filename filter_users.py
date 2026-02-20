import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? "
                          "(Supported filters are 'name', 'age' and 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        while True:
            try:
                age_to_search = input("Enter an age to filter users: ").strip()
                age_to_search = int(age_to_search)
            except ValueError:
                print("Please enter an integer!")
            else:
                filter_users_by_age(age_to_search)
                break
    elif filter_option == "email":
        while True:
            email_to_search = input("Enter a mail address to filter users: ").strip()
            if "@" in email_to_search and email_to_search.split(".")[1] in ("com", "net"):
                filter_users_by_email(email_to_search)
                break
            else:
                print("Please enter a valid mail address!")
    else:
        print("Filtering by that option is not yet supported.")
