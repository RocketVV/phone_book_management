import re

from contact import Contact
import logging
import csv
import json
import utils
import os


class PhoneBook:

    def __init__(self, contacts_file='data/contacts.json'):
        self.contacts = []
        self.contacts_file = contacts_file
        logging.basicConfig(filename='logs/phone_book.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def save_contacts(self):
        contacts_data = [contact.to_dict() for contact in self.contacts]
        # check if we need to make a parent directory
        os.makedirs(os.path.dirname(self.contacts_file), exist_ok=True)
        with open(self.contacts_file, 'w') as file:
            json.dump(contacts_data, file, indent=4, default=str)
        logging.info("Contacts saved to file.")

    def load_contacts(self):
        if os.path.exists(self.contacts_file):
            with open(self.contacts_file, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = [Contact.from_dict(data) for data in contacts_data]
            logging.info("Contacts loaded from file.")
        else:
            self.contacts = []
            logging.warning("No existing contacts file found. Starting with an empty phone book.")

    def add_contact(self, contact):
        self.contacts.append(contact)
        logging.info(f"Added contact: {contact.first_name} {contact.last_name}")

    def batch_import(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    contact = Contact(**row)
                    self.add_contact(contact)
                except ValueError as e:
                    logging.error(f"Error importing contact: {e}")

    def get_contact_by_id(self, contact_id):
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact

    def get_contact(self, **kwargs):
        results = self.contacts
        for key, value in kwargs.items():
            results = [c for c in results if getattr(c, key) == value]
        return results

    def get_next_contact_id(self):
        return max(contact.contact_id for contact in self.contacts) + 1 if len(self.contacts) > 0 else 1

    def update_contact(self, contact, **kwargs):
        contact.update(**kwargs)
        logging.info(f"Updated contact: {contact.first_name} {contact.last_name}")

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        logging.info(f"Deleted contact: {contact.first_name} {contact.last_name}")

    def search_contacts(self, query):
        pattern = re.compile(query, re.IGNORECASE)
        return [c for c in self.contacts if pattern.search(c.first_name) or pattern.search(c.last_name)]

    def filter_contacts_by_date(self, start_date, end_date):
        return [c for c in self.contacts if start_date <= c.created_at <= end_date]

    def sort_contacts(self, key='last_name'):
        return sorted(self.contacts, key=lambda c: getattr(c, key))

    def group_contacts(self):
        groups = {}
        for contact in self.contacts:
            initial = contact.last_name[0].upper()
            groups.setdefault(initial, []).append(contact)
        return groups
