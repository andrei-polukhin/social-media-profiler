import json
import codecs


def dump_to_json(python_object):
    if isinstance(python_object, bytes):
        return {
            "__class__": "bytes",
            "__value__": codecs.encode(python_object, "base64").decode(),
        }
    raise TypeError(repr(python_object) + " is not JSON serializable.")


def load_from_json(json_object):
    if "__class__" in json_object and json_object["__class__"] == "bytes":
        return codecs.decode(json_object["__value__"].encode(), "base64")
    return json_object


def on_login_callback(api_response, new_settings_file):
    # Saving callback after successful login to reuse it
    cache_settings = api_response.settings
    with open(new_settings_file, "w") as outfile:
        json.dump(cache_settings, outfile, default=dump_to_json)
