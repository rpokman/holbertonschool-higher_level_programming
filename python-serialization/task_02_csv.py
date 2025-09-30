#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r") as f:
            data = list(csv.DictReader(f))
        with open("data.json", "w") as out:
            json.dump(data, out)
        return True
    except Exception:
        return False
