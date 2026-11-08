#INITIALISATION OF DECORATOR

def input_error(func):
    """Перехоплює типові помилки введення й повертає користувачу повідомлення."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # не вистачає (або забагато) аргументів для розпакування name, phone
            return "Enter the argument for the command"
        except IndexError:
            # наприклад, args[0] для порожнього списку
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not found."
    return inner


#PROGRAM FUNCTIONS

def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change [name] [new phone]"
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()