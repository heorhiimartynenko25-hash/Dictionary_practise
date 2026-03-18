phonebook = []

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
        print(*phonebook)
