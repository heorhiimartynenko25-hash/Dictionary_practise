phonebook = []
checker = False

while True:
    command = input("enter command: ")
    if command == "exit":
        break
    elif command == "add":
        phonebook.append(
            {"name" : input("Enter name: "),
             "phone": input("Enter phone number: ")}
        )
    elif command == "show":
        for human in phonebook:
            print(human["name"], ' - ', human["phone"])
    elif command == "remove":
        for human in phonebook:
            if human['phone'] == input("Enter phone number: "):
                phonebook.remove(human)
    elif command == "search":
        search_name = input("Enter name: ")
        for human in phonebook:
            if human['name'] == search_name:
                print(f"{human['name']} - {human['phone']}")
                checker = True
        if not(checker):
            print("Not found")
        checker = False
