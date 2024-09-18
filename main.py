import sys
import os

from future.backports.datetime import datetime

from phone_book import PhoneBook
from contact import Contact
import utils


def welcome():
    return input(
        "\n--- Welcome to Phone Book Management Application ---" +
        "\n\nWhat can I do for you?" +
        "\n1. Create Contacts" +
        "\n2. Search Contacts" +
        "\n3. Update Contact" +
        "\n4. Delete Contacts" +
        "\n5. View Contacts" +
        "\n6. Exit" +
        "\n\nEnter your choice here (1-6): "
    ).strip()


def main():
    # Ensure necessary directories exist
    os.makedirs('logs', exist_ok=True)
    os.makedirs('data', exist_ok=True)

    # Instantiate the Phone Book with persistence
    phone_book = PhoneBook()
    # also we can consider to combine the load_contacts() into PhoneBook() init function
    # it makes PhoneBook() easier to use, although it might contradict to the principle of single responsibility
    phone_book.load_contacts()

    while True:
        choice = welcome()

        if choice == '1':
            create_contacts_cli(phone_book)
        elif choice == '2':
            search_contacts_cli(phone_book)
        elif choice == '3':
            update_contact_cli(phone_book)
        elif choice == '4':
            delete_contacts_cli(phone_book)
        elif choice == '5':
            view_contacts_cli(phone_book)
        elif choice == '6':
            # save contacts data before we quit the application
            phone_book.save_contacts()
            print("Exiting the Phone Book Application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


def create_contacts_cli(phone_book):
    while True:
        choice = input(
            "\n--- Create Contacts ---" +
            "\n1. Create New Contact" +
            "\n2. Import Contacts from CSV" +
            "\n3. Back to Main Menu" +
            "\n\nEnter your choice: "
        ).strip()

        if choice == '1':
            first_name = utils.get_non_empty_input("First Name")
            last_name = utils.get_non_empty_input("Last Name")
            phone_number = utils.get_valid_phone_number()
            email_address = utils.get_valid_email()
            address = input("Address (Optional): ").strip()

            contact = Contact(
                contact_id=phone_book.get_next_contact_id(),
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email_address=email_address,
                address=address if address else None
            )
            phone_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            batch_import_contacts_cli(phone_book)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


def batch_import_contacts_cli(phone_book):
    csv_file_path = input("Enter the path to the CSV file: ").strip()
    try:
        phone_book.batch_import(csv_file_path)
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"Error importing contacts: {e}")


def search_contacts_cli(phone_book):
    while True:
        choice = input(
            "\n--- Search Contacts ---" +
            "\n1. Wildcard search" +
            "\n2. Search by date (a specific time frame, start time -> end time)" +
            "\n3. Back to Main Menu" +
            "\n\nEnter your choice:"
        ).strip()

        if choice == '1':
            query = input("Enter search query (use .* for wildcard): ")
            results = phone_book.search_contacts(query)
            utils.print_contacts(results)
        elif choice == '2':
            print('please use the ios time format (yyyy-mm-dd hh:mm:ss) for input')
            start_time = datetime.fromisoformat(input(f"Start Time:"))
            end_time = datetime.fromisoformat(input(f"End Time:"))
            results = phone_book.filter_contacts_by_date(start_time, end_time)
            utils.print_contacts(results)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


def update_contact_cli(phone_book):
    contact_id = input(
        "\n--- Update Contact ---" +
        "\nEnter the Contact ID to update: "
    ).strip()

    if not contact_id.isdigit():
        print("Invalid Contact ID. It must be an integer.")
        return
    contact = phone_book.get_contact_by_id(int(contact_id))

    if contact:
        print(f"Updating Contact: {contact.first_name} {contact.last_name}")

        updates = {}

        # first_name, last_name, phone_number aren't null
        # email_address and address can be optional, so we assign any legitimate value to them
        first_name = utils.get_non_empty_input("First Name")
        updates['first_name'] = first_name

        last_name = utils.get_non_empty_input("Last Name")
        updates['last_name'] = last_name

        phone_number = utils.get_valid_phone_number()
        updates['phone_number'] = phone_number

        email_address = utils.get_valid_email()
        updates['email_address'] = email_address

        address = input(f"Address [{contact.address or 'None'}]: ").strip()
        updates['address'] = address if address else None

        try:
            phone_book.update_contact(contact, **updates)
            print("Contact updated successfully.")
        except ValueError as ve:
            print(f"Error updating contact: {ve}")
    else:
        print(f"No contact found with ID {contact_id}")


def delete_contacts_cli(phone_book):
    ids = input(
        "\n--- Delete Contacts ---" +
        "\nEnter the Contact ID(s) for deletion, split by ','." +
        "\nFor example: 1,2,3" +
        "\n\nContact ID(s):"
    ).strip()

    if not ids:
        print("No IDs. Back to Main Menu.")
        return

    contact_ids = [id.strip() for id in ids.split(',')]
    if not contact_ids:
        print("No valid IDs entered. Back to Main Menu.")
        return

    not_found_ids = []
    deleted_contact_ids = []
    for contact_id in contact_ids:
        if not contact_id.isdigit():
            print("Invalid Contact ID. It must be an integer.")
            return
        contact = phone_book.get_contact_by_id(int(contact_id))
        if contact:
            phone_book.delete_contact(contact)
            deleted_contact_ids.append(contact_id)
            print(f"Deleted contact: {contact.first_name} {contact.last_name} (ID: {contact_id})")
        else:
            not_found_ids.append(contact_id)

    if not_found_ids:
        print(f"The following IDs were not found and could not be deleted: {', '.join(not_found_ids)}")

    if len(deleted_contact_ids) > 0:
        print("Contacts have been deleted successfully.")


def view_contacts_cli(phone_book):
    """CLI function to view contacts."""
    while True:
        choice = input(
            "\n--- View Contacts ---" +
            "\n1. View Contacts Sorted" +
            "\n2. View Contacts Grouped" +
            "\n3. View Contacts History Changes" +
            "\n4. Back to Main Menu" +
            "\n\nEnter your choice: "
        ).strip()

        if choice == '1':
            sort_key = input("Sort by (first_name/last_name): ").strip()
            if sort_key in ['first_name', 'last_name']:
                contacts = phone_book.sort_contacts(key=sort_key)
                utils.print_contacts(contacts)
            else:
                print("Invalid sort key.")
        elif choice == '2':
            groups = phone_book.group_contacts()
            for initial, group in sorted(groups.items()):
                print(f"\nContacts starting with '{initial}':")
                utils.print_contacts(group)
        elif choice == '3':
            view_contact_history_cli(phone_book)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def view_contact_history_cli(phone_book):
    """CLI function to view the history of changes for a contact."""
    contact_id = input(
        "\n--- View Contact History ---" +
        "\nEnter the Contact ID: "
    ).strip()

    if not contact_id.isdigit():
        print("Invalid Contact ID. It must be an integer.")
        return

    contact = phone_book.get_contact_by_id(int(contact_id))
    if contact:
        if contact.history:
            print(f"\nHistory for contact {contact.first_name} {contact.last_name} (ID: {contact.contact_id}):")
            for record in contact.history:
                print(f"\n---------------------------------")
                print(
                    f"\nTimestamp: {datetime.datetime.fromisoformat(record['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}" +
                    f"\nField Changed: {record['field']}" +
                    f"\nOld Value: {record['old_value']}" +
                    f"\nNew Value: {record['new_value']}")
        else:
            print("No history available for this contact.")
    else:
        print(f"No contact found with ID {contact_id}")


if __name__ == '__main__':
    main()
