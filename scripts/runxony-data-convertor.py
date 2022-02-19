#!/usr/bin/env python3

import csv
import json
 
def make_json(csvFilePath, jsonFilePath):
    titleline = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        # only need one line
        for rows in csvReader:
            titleline = rows
            break
    # erase the data
    for key in titleline:
        titleline[key] = ""
    # write with json format
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(titleline, indent=4))

def gen_csv_line_from_json(jsonFile):
    with open(jsonFilePath, 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
        csvline = ""
        for key in data:
            if len(data[key]) > 0 :
                csvline += "\"" + data[key] + "\","
            else:
                csvline += ","
        print(csvline)

csvFilePath = r'runXonY.csv'
jsonFilePath = r'csv-titles-with-empty-data.json'
 
# make_json(csvFilePath, jsonFilePath)
gen_csv_line_from_json(jsonFilePath)
