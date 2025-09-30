#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary into JSON
    and save it to the given filename.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON from a file and deserialize it
    back into a Python dictionary.
    """
    with open(filename, "r") as f:
        return json.load(f)
