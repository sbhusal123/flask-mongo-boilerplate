import json


def convert_dict_to_string(dict_data):
    """Converts dit to string"""
    return json.dumps(dict_data)


def convert_string_to_dict(string_data):
    """Converts string to dict"""
    return json.loads(string_data)


def get_datetime_difference(initial, final):
    """Returns time difference from two objects of datetime in second"""
    time_difference = (final - initial).total_seconds()
    return time_difference
