import re

class ContactBook:
    """
    A simple contact book to save, get, update, and show contacts.
    """
    def __init__(self):
        self.contacts = {}

    def input_error(func):
        """
        Decorator to handle input errors.
        """
        func_usage = {'save_contact': 0, 'get_contact': 0, 'update_contact': 0, 'show_all_contacts': 0}

        def handler(*args, **kwargs):
            try:
                func_usage[func.__name__] += 1
                func(*args, **kwargs)
                return
            except IndexError:
                print("Unknown command. Please try again.")
                return
            except ValueError:
                print("Invalid phone number format. Make sure to provide a valid phone number.")
                return
            except TypeError:
                print("Make sure to provide the correct number of arguments.")
                return
            except KeyError:
                print("Contact not found. Make sure to save the contact first.")
                return
        return handler
    
    @input_error
    def save_contact(self, name: str, phone: str):
        """
        Save name and phone number.
        """
        self.contacts[name] = self.normalize_phone(phone)
        print("Contact saved.")

    @input_error
    def get_contact(self, name: str):
        """
        Get phone number by name.
        """
        print(self.contacts.get(name))

    @input_error
    def update_contact(self, name: str, phone: str):
        """
        Update phone number for existing contact.
        """
        self.contacts[name]  # Check if contact exists
        self.contacts[name] = self.normalize_phone(phone)
        print("Contact updated.")

    @input_error
    def show_all_contacts(self):
        """
        Show all saved contacts.
        """
        for name, phone in self.contacts.items():
            print(f"Name: {name}, Phone: {phone}")

    def normalize_phone(self, phone_number: str) -> str:
        """
        Normalize a phone number to the format +380XXXXXXXXX.
        :param phone_number: str The input phone number in various formats.

        Return: str The normalized phone number or an empty string if invalid.
        """
        if phone_number[0] == "+":
            phone_number = phone_number.removeprefix("+38")
        elif phone_number.startswith("38"):
            phone_number = phone_number.removeprefix("38")
        phone_number = phone_number.replace(" ","")

        found_number = re.findall(r"(\d{3})[\s\t()\n-]*(\d{3})[\s\t()\n-]*(\d{2})[\s\t()\n-]*(\d{2})", phone_number)

        if found_number:
            return f"+38{found_number[0][0]}{found_number[0][1]}{found_number[0][2]}{found_number[0][3]}"
        else:
            raise ValueError

def parse_input(string: str):
    """
    Parse user input and return command and arguments.
    """
    parts = string.split(" ")
    if len(parts) == 1:
        return parts[0].lower(), []
    elif len(parts[0]) > 1:
        return parts[0].lower(), parts[1:]
    else:  
        return None, []

def main():
    """
    Main function to run the contact book bot.
    """
    contact_book = ContactBook()
    print("Welcome to the Contact Book Bot!")
    print("""Available functions and commands: 
          * save <name> <phone> - Save a new contact
          * get <name> - Get a contact's phone number
          * change/update <name> <phone> - Update an existing contact
          * show all - Show all contacts
          * close/exit - Exit the bot
          """)
    while True:
        user_input = input("Enter command: ")
        command, *args = parse_input(user_input)

        if command in ["add", "save"]:
            contact_book.save_contact(*args[0])
        elif command in ["change", "update"]:
            contact_book.update_contact(*args[0])
        elif command in ["show", "phone"]:
            contact_book.get_contact(*args[0])
        elif command in ["show all", "all"]:
            contact_book.show_all_contacts()
        elif command in ["exit", "close", "good bye"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()