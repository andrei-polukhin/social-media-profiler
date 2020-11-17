# -*- coding: utf-8 -*-
"""The Instagram scraping module to handle cookie settings file."""

import json
import codecs


def dump_to_json(python_object: object) -> dict:
    """
    Dump to JSON using custom schema (see code).

    Args:
        `python_object`: the python object to serialize.
    Returns:
        `dict`: serialized JSON object as a Python dict.
    Raises:
        ``TypeError``: if `python_object` is not JSON-serializable.
    """
    if isinstance(python_object, bytes):
        return {
            "__class__": "bytes",
            "__value__": codecs.encode(python_object, "base64").decode(),
        }
    raise TypeError(repr(python_object) + " is not JSON-serializable.")


def load_from_json(json_object: dict) -> object:
    """
    Load from JSON using custom schema (see code).

    Args:
        `json_object`: serialized JSON object as a Python dict.
    Returns:
        `python_object`: object hook for `json.load` function.
    """
    if "__class__" in json_object and json_object["__class__"] == "bytes":
        return codecs.decode(json_object["__value__"].encode(), "base64")
    return json_object


def on_login_callback(api_response, new_settings_file):
    """
    Save callback after successful login to re-use it.

    Args:
        `api_response`: response from Instagram API.\n
        `new_settings_file`: the name of file to create in a current directory.
    """
    cache_settings = api_response.settings
    with open(new_settings_file, "w") as outfile:
        json.dump(cache_settings, outfile, default=dump_to_json)
