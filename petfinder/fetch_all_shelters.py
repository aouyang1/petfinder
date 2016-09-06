from Petfinder import Petfinder
import os
from pprint import pprint
import json
import csv
from time import sleep


def get_zip_codes():
    f_zip = open('postal_codes.csv','r')
    f_data = csv.reader(f_zip)

    zip_codes = []
    for record in f_data:
        zip_code = record[0]
        if len(zip_code) > 0:
            try:
                zip_int = int(zip_code)
                zip_codes.append(zip_code)
            except:
                print("must be a number as string")

    return zip_codes


PF_KEY=os.environ["PF_KEY"]
p = Petfinder(PF_KEY)

f = open('shelter.json', 'w')

page_size = 1000

shelter_dict = {}

zip_codes = get_zip_codes()

for zipcode in zip_codes:
    sleep(1)
    print("fetching zipcode: {}".format(zipcode))
    try:
        shelters = p.shelter_find(location=str(zipcode),count=page_size)
        for shelter in shelters:
            if shelter["id"] not in shelter_dict:
                shelter_dict[shelter["id"]] = 1

                print(shelter["state"], shelter["city"], shelter["id"], len(shelter_dict))
                f.write("{}\n".format(json.dumps(shelter)))
            else:
                print("shelter id: {} already found".format(shelter["id"]))
    except:
        print("zipcode not found: {}".format(zipcode))

