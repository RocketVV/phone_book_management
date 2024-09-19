import datetime
import re


def get_current_time():
    return datetime.datetime.now()


def validate_phone_number(phone_number):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        return phone_number
    else:
        raise ValueError("Phone number must be in the format (###) ###-####")


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return email
    else:
        raise ValueError("Invalid email address")


def get_non_empty_input(prompt: str):
    """some fields require non-empty input, we use this function for generic usage"""
    while True:
        user_input = input(prompt + ": ").strip()
        if user_input:
            return user_input
        else:
            print(prompt + " cannot be empty. Please enter a valid " + prompt + ".")


def get_valid_phone_number():
    """wrapper: tell the user, we need a valid phone number."""
    while True:
        phone_number = input("Phone Number (###) ###-####: ").strip()
        try:
            return validate_phone_number(phone_number)
        except ValueError as ve:
            print(f"Error: {ve}")


def get_valid_email():
    """wrapper: tell the user, we need a valid email address."""
    while True:
        email_address = input("Email Address (Optional): ").strip()
        if not email_address:
            # Clear the email address
            return None
        try:
            return validate_email(email_address)
        except ValueError as ve:
            print(f"Error: {ve}")


def print_contacts(contacts):
    """Helper function to print a list of contacts."""
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"\n---------------------")
        print(f"Contact ID: {contact.contact_id} ")
        print(f"Name: {contact.first_name} {contact.last_name}")
        print(f"Phone: {contact.phone_number}")
        if contact.email_address:
            print(f"Email: {contact.email_address}")
        if contact.address:
            print(f"Address: {contact.address}")
        print(f"Created At: {contact.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Updated At: {contact.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
