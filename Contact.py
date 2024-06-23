import re
import json
contacts = {}


# opens the backup file with write
# dumps all of the contents of the contacts dict into the file
def backup_contacts(contacts):
    with open('contacts_backup.json', 'w') as file:
        json.dump(contacts, file)
    print("Contacts have been successfully backed up.")
# Opens the designated backup file in read
# loads its contents to a a variable
# checks if it is a dict
# updates the global contacts dictionary with the contact_restore file
def restore_contacts():
    global contacts
    try:
        with open('contacts_backup.json', 'r') as file:
            contact_restore = json.load(file)
        if not isinstance(contacts, dict):
            print('contacts varaible is not a dictionary')
        contacts.update(contact_restore)
        print('contacts restored!')
              
        
    except FileNotFoundError:
        print("Backup file not found.")
    except json.JSONDecodeError:
        print("Error decoding the backup file. Please ensure the file format is correct.")
    except Exception as e:
        print(f"An unexpected error occurred while restoring contacts: {e}")
        
# Takes an input of a filename, opens it with append
# creates a string variable with all of the values for each contact formatted properly
# then writes them to the given file
def export_contacts(contacts):
    filename = input('Enter the name of the file you would like to export to')
    with open(filename, 'a') as file:
        for number, details in contacts.items():
            contact = f'''
{details['name']}
{number}
{details['email']}
{details['address']}
{details['notes']}
{details['groups']} \n\n'''
        
            file.write(contact)
    print(f'files have been succesfully added to {filename}')


# Takes an input of filename
# opens the file with read
# parses the contact details out of the text by stripping and splitting them by 2 new lines, which is the indicator for a new contact
# creates a list of details by splitting them by 1 new line, these are the details of the individual contact
# if the list matches the correct length of 6 (ik ik low functionality well i dont understnad the json or csv module yet so blah)
# unpacks details into the variables then adds them to contacts 
def import_contacts(filename=None):
    global contacts
    if filename is None:
        filename = input('enter the filename of the file you want to import contacts from: ')
    try:
        with open(filename, 'r') as file:
            contact_details = file.read().strip().split('\n\n') # only works if the contacts are split by a blank line, I suppose you can use a regex pattern but its 11 and im tired
            
            for details in contact_details:
                list_of_details = details.strip().split('\n')
                
                # Just Unpacking the list of details it has to match this format exactly to work, has to be exactly six lines long for the parsing
                if len(list_of_details) == 6:
                    name, number, email, address, notes, groups = list_of_details
                    contacts[number] = {
                        'name': name.lower(),
                        'email': email.lower(),
                        'address': address.lower(),
                        'notes': notes.lower(),
                        'groups': groups.lower()
                }
                else:
                    print(f"Skipping invalid contact entry: {details}")
    except Exception as e:
        print(f'''
Error: Make sure your file is formatted as follows:

(Contact)
name
number
email
address
notes
groups

(Contact)
etc...
more info: {e}''')


# Takes an input of contacts and sorts the list based off of the input 
# if choice is one it displays by grouping
# if choice is 2 it displays alphabetically by name
# if 3 displays alphabetically by email
def view_contacts(contacts):
    
    view_choice = input('''
How would you like to display your contacts?
1. By Groups
2. Alphabetically by name 
3. Alphabetically by email                   
Enter the Corresponding number for the Display Type''')
    if view_choice == '1':
        if contacts:
            try:
                groups = {}
                for number, details in contacts.items():
                    contact_groups = details['groups'].split(',')

                    for group in contact_groups:
                        if group not in groups:
                            groups[group] = []
                    
                        groups[group].append({
                            'number': number,
                            'name': details['name'],
                            'email': details['email'],
                            'address': details['address'],
                            'notes': details['notes'],
                            'groups': ', '.join(contact_groups)
                    })
                for group, members in groups.items():
                    print(f'''
----------Group: {group.title()}-----------
''')
                    for member in members:
                        print(f""" 
~~~ Name:{member['name']} ~~~
    Number: {member['number']}
    Email: {member['email']}
    Address: {member['address']} 
    Notes: {member['notes']} 
    Groups: {member['groups']}""")
                    print('\n')
            except:
                print('hmm had an error')
        else:
            print('Your Contacts list is empty')
    elif view_choice == '2':
        if contacts:
            try:
                contacts_list = []
                for number, details in contacts.items():
                    contact_info = {
                        'number': number,
                        'name': details['name'],
                        'email': details['email'],
                        'address': details['address'],
                        'notes': details['notes'],
                        'groups': details['groups']
                    }
                    contacts_list.append(contact_info)
                    
                sorted_contacts = sorted(contacts_list, key=lambda x: x['name'].lower())
                for contact in sorted_contacts:
                    print(f"""
-----Name: {contact['name']}-----
    Number: {contact['number']} 
    Email: {contact['email']} 
    Address: {contact['address']} 
    Notes: {contact['notes']} 
    Groups: {contact['groups']}
    """)
            except:
                print('Hm there is an error lurking here somewhere')
        else:
            print('Your Contacts list is Empty!')
    elif view_choice == '3':
        if contacts:
            try:
                contacts_list = []
                for number, details in contacts.items():
                    contact_info = {
                        'number': number,
                        'name': details['name'],
                        'email': details['email'],
                        'address': details['address'],
                        'notes': details['notes'],
                        'groups': details['groups']
                    }
                    contacts_list.append(contact_info)
                    
                sorted_contacts = sorted(contacts_list, key=lambda x: x['email'].lower())
                for contact in sorted_contacts:
                    print(f"""
------Email: {contact['email']}------ 
      Name: {contact['name']}
      Number: {contact['number']}
      Address: {contact['address']}
      Notes: {contact['notes']}
      Groups: {contact['groups']}
      """)
            except:
                print('Hm there is an error lurking here somewhere')
        else:
            print('Your Contacts list is Empty!')
    else:
        print('Please enter a valid input: 1-3.')


# takes a search query
# initializes a flag as false
# iterates through the keys of each contact number 
# sets a var search_value to number and all of its details
# checks if search_query is in any value in the list
# (side note: why didnt we learn the any function?? crazy powerful.)
# returns the details of the function if found and flips the flag
def search_for_contact(contacts):
    search_query = input('Enter your search query: ').lower()  
    found = False

    for number, details in contacts.items():
        search_values = [number] + list(details.values())
        if any(search_query in str(value).lower() for value in search_values):
            print(f'''
Contact Found:
Name: {details['name']}
Number: {number}
Email: {details['email']}
Address: {details['address']}
Notes: {details.get('notes', 'N/A')}
Groups: {details.get('groups', 'N/A')}''')
            found = True
            break  

    if not found:
        print('Contact not found!')






# initializes a dict called groups 
# iterates through the contact keys
# creates a variable called contact groups that is all group values of the contacts
# adds them all to the group dict
# appends all the details of items that belong to the group as a key 
# prints all of the the groups and their contacts
# \\\\\\side note: made this group view so you could see what you were going to delete but it
#                  ended up informing me for all of my display options as well
# The delete function was the easiest part of this function lol
def delete_contact(contacts):
    if contacts:
            try:
                groups = {}
                for number, details in contacts.items():
                    contact_groups = details['groups'].split(',')

                    for group in contact_groups:
                        if group not in groups:
                            groups[group] = []
                    
                        groups[group].append({
                            'number': number,
                            'name': details['name'],
                            'email': details['email'],
                            'address': details['address'],
                            'notes': details['notes'],
                            'groups': ', '.join(contact_groups)
                    })
                for group, members in groups.items():
                    print(f'''
----------Group: {group.title()}-----------
''')
                    for member in members:
                        print(f""" 
~~~ Name:{member['name']} ~~~
    Number: {member['number']}
    Email: {member['email']}
    Address: {member['address']} 
    Notes: {member['notes']} 
    Groups: {member['groups']}""")
                    print('\n')
            except:
                print('hmm had an error')
    else:
        print('Your Contacts list is empty')
                
    contact_to_del = input("Enter the number of the contact You would like to delete: ")
    if contact_to_del in contacts:
        del contacts[contact_to_del]
        print(f'{contact_to_del} was removed from your contacts list.')
    else:
                print('Contact not found.')
    
            

    
    
# uses the same view as delete so you can see what you are going to edit
# takes an input for the contact you want to edit and the field
# initializes a new_value variable that is the input for the field you are editing
# sets the contacts field to the new_value input
# can probably put my number pattern in here to validate if the number is correctly formatted,
# or should i refactor my code so instead of validation it just formats whatever is input? idk its 2am im tired. 
def edit_contact(contacts):
    if contacts:
        try:
            groups = {}
            
            for number, details in contacts.items():
                contact_groups = details['groups'].split(',')

                for group in contact_groups:
                    if group not in groups:
                        groups[group] = []
                    
                    groups[group].append({
                        'number': number,
                        'name': details['name'],
                        'email': details['email'],
                        'address': details['address'],
                        'notes': details['notes'],
                        'groups': ', '.join(contact_groups)
                    })
            for group, members in groups.items():
                print(f'Group: {group}')
                for member in members:
                    print(f" Name:{member['name']}, Number: {member['number']}, Email: {member['email']}, Address: {member['address']}, Notes: {member['notes']}, Groups: {member['groups']}")
                print('\n')
            contact_to_edit = input('Enter the number of the contact you would like to edit: ')
            field_to_edit = input('Enter the name of the field you would like to edit in the contact: ').lower().strip()
            if contact_to_edit in contacts:
                if field_to_edit in contacts[contact_to_edit]:
                    new_value = input(f'Enter the new value for {field_to_edit}: ').lower()
                    contacts[contact_to_edit][field_to_edit] = new_value
                    print(f"{field_to_edit.capitalize()} updated to: {new_value}")
                else:
                    print(f"The field '{field_to_edit}' does not exist in the contact's details.")
            else:
                print("Contact not found.")
        except:
            print('Ran into an error, Try again')  
    else:
        print('Your contacts list is empty')                 

# Takes an input for the number, validates it against my number pattern
# takes a name input
# takes an email input validates it against my email pattern
# takes an address and notes pattern
# takes an group input and makes sure that if their are more than one value it is a csv
# appends all to contacts
def add_contact(contacts):
    # Takes an input of a # checks to see if the number follows the correct format for the pattern
    number = input("Enter the number of the contact in the following order: (***) ***-****: ")
    number_pattern = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')
    if not number_pattern.match(number):
        print("Invalid number format")
        return add_contact(contacts)

    name = input("Enter the name of the number owner: ").lower()
    # takes an email input and validates the email against an email pattern
    email = input('Enter the Email associated with the phone number: ').lower()
    email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
    if not email_pattern.match(email):
        print('Invalid Email format')
        return add_contact(contacts)

    address = input('Enter the address of the phone owner: ').lower()
    notes = input('Notes: ').lower()
    # Takes one or more groups and makes sure the values are comma-seperated and makes them lower case(used for later call back)
    group = input("Enter the group this contact belongs to (if you would like to add multiple make them comma seperated ie family,friends): ").lower()
    group_pattern = re.compile(r'^[a-zA-Z0-9]+(,[a-zA-Z0-9]+)*$')
    if not group_pattern.match(group):
        print("Invalid group format. Please use comma-separated values with no spaces.")
        return add_contact(contacts)
    
    contacts[number] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes,
        'groups': group  
    }

    print(f'Contact {name} added successfully.')
            
# CAPN OF THE SHIP   
def main(contacts):
    while True:
        menu_choice = input("""
Enter The Number that corresponds with the action you would like to take:

1. Add new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a .txt file
7. Import Contacts from a text file
8. Backup Contacts
9. Restore Contacts
10. QUIT

Your Choice: """)
        if menu_choice == '1':
            add_contact(contacts)
        elif menu_choice == '2':
            edit_contact(contacts)
        elif menu_choice == '3':
            delete_contact(contacts)
        elif menu_choice == '4':
            search_for_contact(contacts)
        elif menu_choice == '5':
            view_contacts(contacts)
        elif menu_choice == '6':
            export_contacts(contacts)
        elif menu_choice == '7':
            import_contacts(filename=None)
        elif menu_choice == '8':
            backup_contacts(contacts)
        elif menu_choice == '9':
            restore_contacts()
        elif menu_choice == '10':
            print('Shuttin down...')
            break
        else:
            print("Please enter a valid input")
            
main(contacts)