#!/usr/bin/env python

import json
import os


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "data/gamemaster.json"
abs_file_path = os.path.join(script_dir, rel_path)

master_dict = {}
with open(abs_file_path, "r") as f:
    master_dict = json.load(f)

for entry in master_dict["pokemon"]:
    print(entry["speciesName"])
