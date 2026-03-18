phonebook = []
checker = False

while True:
    command = input("enter command: ")
    if command == "exit":
        break

    elif command == "add":
        input_name = input("Enter name: ")
        input_phone = input("Enter phone number: ")

        for human in phonebook:
            if human['phone'] == input_phone:
                print(f"{human['name']} already has this number. Maybe, an error occured.")
                checker = True

        if not(checker):
            phonebook.append(
                {"name" : input_name,
                 "phone": input_phone}
            )
        checker = False

    elif command == "show":
        for human in phonebook:
            print(human["name"], ' - ', human["phone"])

    elif command == "remove":
        for human in phonebook:
            if human['phone'] == input("Enter phone number: "):
                phonebook.remove(human)

    elif command == "search":
        search_type = input("by name / by phone: ")
        if search_type == 'by name':
            search_name = input("Enter name: ")
            for human in phonebook:
                if human['name'] == search_name:
                    print(f"{human['name']} - {human['phone']}")
                    checker = True
            if not(checker):
                print("Not found")
            checker = False
        elif search_type == 'by phone':
            search_phone = input("Enter phone number: ")
            for human in phonebook:
                if human['phone'] == search_phone:
                    print(f"{human['name']} - {human['phone']}")
                    checker = True
            if not(checker):
                print("Not found")
            checker = False
