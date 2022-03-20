from .utils import (
    convert_dict_to_string,
    convert_string_to_dict,
    get_datetime_difference,
)
from .fernet import FernetHelper

import datetime
from dateutil import parser


class Token(object):
    """Token encode decode helper"""

    def __init__(self, ttl_in_second=15*60):
        """Takes time to live in second: defaults to 15sec"""
        self.fernet = FernetHelper()
        self.ttl_in_second = ttl_in_second

    def __add_expiry_time(self, data):
        """Adds expiry time to the data."""
        data_dict = {"data": data, "expiry": str(datetime.datetime.now())}
        string_data_dict = convert_dict_to_string(data_dict)
        return string_data_dict

    def get_token(self, data):
        """Returns encrypted token with the expiry date. Date also encrypted"""
        expiry_added_data = self.__add_expiry_time(data)
        encrypted_data = self.fernet.encrypt(expiry_added_data)
        return encrypted_data

    def __is_token_valid(self, data_dict):
        """Accepts the dict of decrtpted data and checks if it's valid"""

        # check if data dicts contains valid keys
        data = data_dict.get("data", None)
        expiry = data_dict.get("expiry", None)
        is_token_valid = data != None or expiry != None

        # Check if token is expired
        time_difference = get_datetime_difference(
            parser.parse(expiry), datetime.datetime.now()
        )

        is_not_expired = time_difference < float(self.ttl_in_second)

        if is_token_valid and is_not_expired:
            return True
        return False

    def get_data(self, cipher_text):
        """Returns and checks actual data after decrypting"""
        decrypted_token = self.fernet.decrypt(cipher_text)

        if not decrypted_token:
            return "Invalid token"

        data_dict = convert_string_to_dict(decrypted_token)

        if self.__is_token_valid(data_dict):
            return data_dict.get("data")
        else:
            return False


"""
# Initialize JWT with time to live in second.
t = Token(ttl_in_second=2)

data = "my awesome data"
token = t.get_token(data)
print(token)

print("\n")
text = t.get_data(token)
print(text)
"""
