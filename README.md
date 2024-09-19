# Phone Book Management Application

A simple command-line application for managing your phone book contacts.

## Requirements

Python 3.6 or higher

## Features

- Create Contacts:
    - create new contacts with basic details.
    - add multiple contacts from a CSV file.
- Search Contacts: Find contacts by name or other details (phone number, etc.).
- Update Contacts: Modify existing contact information.
- Delete Contacts: Remove contacts individually or in batches.
- View Contacts:
    - by sorting based on alphabetical order.
    - in group by the initial letter of the last name.
    - view contact history: see a record of changes made to contacts.
- Data Persistence: Contacts are saved to a JSON file (when user quit the application) for future use.

## Project Structure

```shell
phone-book-management/
├── main.py            # The main application entrance
├── contact.py         # Contact class
├── phone_book.py      # PhoneBook class
├── utils.py           # Utilities class 
├── data/
│   └── contacts.json  # JSON file storing contact data
├── logs/
│   └── phone_book.log # Log file for operations
├── test_data/
│   └── fake_data.csv  # fake CSV data for testing contacts batch import
├── README.md          # Project documentation
```

## Getting Started

1. Clone the Repository

```shell
git clone https://github.com/RocketVV/phone_book_management.git
cd phone_book_management
```

or unzip from the `phone_book_management.zip` file and open it

2. Run the Application under the root directory

```shell
python3 main.py
```

## Main Menu

Upon running, you’ll see the main menu:

```shell
--- Welcome to Phone Book Management Application ---

What can I do for you?
1. Create Contacts
2. Search Contacts
3. Update Contact
4. Delete Contacts
5. View Contacts
6. Exit

Enter your choice here (1-6): 
```

Enter the number corresponding to the action you wish to perform.

### Create contacts

There are 2 ways of creating contacts: in single or batch mode.

```shell
--- Create Contacts ---
1. Create New Contact
2. Import Contacts from CSV
3. Back to Main Menu

Enter your choice:
```

#### Creating a single contact

```shell
Enter your choice: 1

First Name: John
Last Name: Dow
Phone Number (###) ###-####: (123) 456-7890
Email Address (Optional): john.doe@example.com
Address (Optional): 123 Main St
Contact added successfully.
```

#### Importing contacts form CSV file

```shell
Enter your choice: 2
Enter the path to the CSV file: ./test_data/fake_data.csv
Contacts imported successfully.
```

### Searching Contacts

There are 2 ways of searching contacts:

```shell
--- Search Contacts ---
1. Wildcard search
2. Search by date (a specific time frame, start time -> end time)
3. Back to Main Menu
```

#### Wildcard search

```shell
Enter your choice:1
Enter search query (use .* for wildcard): John

---------------------
Contact ID: 35 
Name: Jennifer Johnson
Phone: (405) 427-2071
Email: cmorgan@gmail.com
Address: PSC 8145, Box 8759
APO AA 96045
Created At: 2022-08-30 17:27:00
Updated At: 2021-03-03 05:45:22
```

#### Search by date

```shell
Enter your choice:2
please use the ios time format (yyyy-mm-dd hh:mm:ss) for input
Start Time:2021-12-04 05:28:59
End Time:2022-01-04 05:28:59

---------------------
Contact ID: 34 
Name: Sara Jones
Phone: (391) 738-3377
Email: iramos@gmail.com
Address: 9396 Andre Bridge Apt. 187
South Reneeberg, NY 22216
Created At: 2021-12-10 17:51:05
Updated At: 2023-05-02 11:22:05

```

### Update Contact

1. Enter Contact ID: Provide the integer Contact ID of the contact you wish to update.
2. Update Fields: Press `Enter` to keep the current value or input a new value.

```shell
--- Update Contact ---
Enter the Contact ID to update: 6
Updating Contact: Michael Banks
First Name [Michael]: Mike
Last Name [Banks]: 
Nothing changed. Keeping the current value.
Phone Number [(135) 992-7140]: (123) 456-7890
Email Address [owengabriel@ruiz.org]: 
Nothing changed. Keeping the current value.
Address [Unit 2493 Box 7701
DPO AA 89953]: 
Nothing changed. Keeping the current value.
Contact updated successfully.
```

### Delete Contacts

Input one contact ID or multiple Contact IDs separated by commas for deletion.

```shell
--- Delete Contacts ---
Enter the Contact ID(s) for deletion, split by ','.
For example: 1,2,3

Contact ID(s):5,8,9
Deleted contact: Connie Smith (ID: 5)
Deleted contact: Raymond Chang (ID: 8)
Deleted contact: Raymond Floyd (ID: 9)
Contacts have been deleted successfully.
```

### View Contacts

```shell
--- View Contacts ---
1. View Contacts Sorted
2. View Contacts Grouped
3. View Contacts History Changes
4. Back to Main Menu
```

1. View Contacts by sorting based on alphabetical order.

```shell
Enter your choice: 1

---------------------
Contact ID: 22 
Name: Jonathan Adams
Phone: (275) 233-4030
Email: scarlson@gmail.com
Address: 488 Morales Port
Younghaven, AL 97218
Created At: 2022-11-02 17:26:31
Updated At: 2022-01-04 02:17:07

---------------------
Contact ID: 43 
Name: Kevin Allen
Phone: (737) 245-5906
Email: csanchez@davila.com
Address: 9565 Huerta Glen
North Kathrynborough, CT 00912
Created At: 2020-09-02 12:44:19
Updated At: 2021-02-19 20:43:19

```

2. View Contacts in group by the initial letter of the last name.

```shell
Enter your choice: 2
Contacts starting with 'A':

---------------------
Contact ID: 2 
Name: hfiosa afsa
Phone: (124) 456-3452
Email: fdsfds@gc.com
Address: fdsafs street
Created At: 2024-09-18 16:13:22
Updated At: 2024-09-18 16:13:22

---------------------
Contact ID: 22 
Name: Jonathan Adams
Phone: (275) 233-4030
Email: scarlson@gmail.com
Address: 488 Morales Port
Younghaven, AL 97218
Created At: 2022-11-02 17:26:31
Updated At: 2022-01-04 02:17:07

```

3. View Contact History: see a record of changes made to contacts.

```shell
Enter your choice: 3

--- View Contact History ---
Enter the Contact ID: 1

History for contact jgg faa (ID: 1):

---------------------------------

Timestamp: 2024-09-18 19:46:37
Field Changed: first_name
Old Value: dsa
New Value: jgg

---------------------------------

Timestamp: 2024-09-18 19:46:37
Field Changed: last_name
Old Value: dsa
New Value: faa

```

## Data Storage

- Contacts are stored in data/contacts.json.
- Logs are saved in logs/phone_book.log.

## Future TODO List
- Export Contacts: Ability to export contacts to a CSV or JSON file.
- GUI Interface: Developing a graphical UI for better UX.
- Security Enhancement: Adding encryption for sensitive data.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.