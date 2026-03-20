def look_for_repetitions_dict(list_of_dicts: list, key_to_compare: str, value) -> list:

    """

    :param list_of_dicts: list of dictionaries to look through
    :param key_to_compare: key to compare
    :param value: value to compare
    :return: empty list if the value is new, list of indexes with same value otherwise
    """
    repetitions_id = []
    for i in range(len(list_of_dicts)):
        if list_of_dicts[i][key_to_compare] == value:
            repetitions_id.append(i)

    return repetitions_id

def is_name_allowed(name: str, allowed_symbols) -> bool:
    for symbol in name:
        if symbol not in allowed_symbols:
            return False

    return True


phonebook = []
checker = False
symbols_phone = '0123456789-'

while True:
    command = input("enter command: ")

    if command == "exit":
        break

    elif command == "add":
        input_name = input("Enter name: ")
        if not input_name == "/..":
            input_phone = input("Enter phone number: ")
            if not input_phone == "/..":

                while input_name != "/.." and input_phone != "/..":

                    if is_name_allowed(input_phone, symbols_phone):

                        repetitions_id = look_for_repetitions_dict(phonebook, "phone", input_phone)
                        if len(repetitions_id) == 0:
                            phonebook.append({
                                "name": input_name,
                                "phone": input_phone
                            })
                            break
                        else:
                            print(phonebook[repetitions_id[0]]["name"] + " already has this phone number. Try again.")
                            input_phone = input("Enter phone number: ")

                    else:
                        print("Phone numbers can contain only digits and '-' symbol. Try again.")
                        input_phone = input("Enter phone number: ")

    elif command == "show":
        for human in phonebook:
            print(human["name"], ' - ', human["phone"])

    elif command == "remove":
        entry = input("Who do you want to remove? ")
        to_remove = []

        if is_name_allowed(entry, symbols_phone):
            print("Assuming phone. Searching...")
            to_remove = look_for_repetitions_dict(phonebook, "phone", entry)
            if len(to_remove) == 0:
                print("No entries were found.")
            else:
                print("Going to remove: " + phonebook[to_remove[0]]['name'] + " - " + phonebook[to_remove[0]]['phone'] + ". Are you sure? Y/N")
                confirmation = input()
                if confirmation == "Y" or confirmation == "y":
                    phonebook.pop(to_remove[0])
                    print("Removed successfully.")
                else:
                    print("Remove cancelled successfully.")

        else:
            print("Assuming name. Searching...")
            to_remove = look_for_repetitions_dict(phonebook, "name", entry)

            if len(to_remove) == 0:
                print("No entries were found.")
            else:
                print("Going to remove:", "\n")
                for i in range(len(to_remove)):
                    print(f"{i+1}.", phonebook[to_remove[i]]['name'], " - ", phonebook[to_remove[i]]['phone'], end=",\n")
                print("\nare you sure? Y/N")
                confirmation = input()

                if confirmation.lower() == "y":
                    for i in range(len(to_remove)):
                        phonebook.pop(to_remove[i] - i)
                    print("Removed successfully.")
                else:
                    print("Remove cancelled successfully.")




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
