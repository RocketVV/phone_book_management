import datetime
import utils
import logging


class Contact:
    """A class to represent a contact object in the phone book."""

    def __init__(self, contact_id: int, first_name, last_name, phone_number, email_address=None, address=None,
                 created_at=None, updated_at=None, history=None):
        self.contact_id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = utils.validate_phone_number(phone_number)
        self.email_address = utils.validate_email(email_address) if email_address else None
        self.address = address
        self.created_at = created_at if created_at else utils.get_current_time()
        self.updated_at = updated_at if updated_at else utils.get_current_time()
        self.history = history if history else []

    def update(self, **kwargs):
        """Update contact details and history changes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                old_value = getattr(self, key)
                setattr(self, key, value)
                change_record = {
                    'timestamp': utils.get_current_time(),
                    'field': key,
                    'old_value': old_value,
                    'new_value': value
                }
                self.history.append(change_record)
                self.updated_at = utils.get_current_time()
                logging.info(
                    f"Updated contact {self.first_name} {self.last_name}: {key} changed from {old_value} to {value}")

    def to_dict(self):
        """Convert the contact object to a dictionary for JSON serialization."""
        return {
            'id': self.contact_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email_address': self.email_address,
            'address': self.address,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'history': self.history
        }

    def __str__(self):
        return f"Contact {self.first_name} {self.last_name} {self.phone_number} {self.email_address} {self.address}"

    @classmethod
    def from_dict(cls, data):
        """Create a Contact object from a dictionary."""
        return cls(
            contact_id=int(data.get('id')),
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            email_address=data.get('email_address'),
            address=data.get('address'),
            created_at=datetime.datetime.fromisoformat(data.get('created_at')),
            updated_at=datetime.datetime.fromisoformat(data.get('updated_at')),
            history=data.get('history', [])
        )
