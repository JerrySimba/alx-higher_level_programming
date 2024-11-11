people = []

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name": name,
        "age": age,
        "email": email
    }
    return person

def delete_person(people):
    if not people:
        print("No people to delete.")
        return
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

    try:
        to_delete = int(input("Enter the number of the person to delete: ")) - 1
        if 0 <= to_delete < len(people):
            removed_person = people.pop(to_delete)
            print(f"{removed_person['name']} has been deleted.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def search_person():
    name_to_search = input("Enter the name to search: ").lower()
    found_people = [person for person in people if person["name"].lower() == name_to_search]
    if found_people:
        for person in found_people:
            print(f"Found: {person['name']} | {person['age']} | {person['email']}")
    else:
        print("No person found with that name.")

print("Hi, welcome to the CMS.\n")

while True:
    command = input("You can 'add', 'delete', 'search', or 'quit': ").lower()
    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added successfully.")
    elif command == "delete":
        delete_person(people)
    elif command == "search":
        search_person()
    elif command == "quit":
        print("Exiting the CMS.")
        break
    else:
        print("Invalid command!")

print("People in the system:", people)
