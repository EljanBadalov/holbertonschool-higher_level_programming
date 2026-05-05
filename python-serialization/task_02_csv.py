#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename, json_filename="data.json"):
    try:
        data = []

        with open(csv_filename, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open(json_filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (FileNotFoundError, IOError):
        return False
