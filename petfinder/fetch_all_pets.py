from Petfinder import Petfinder
import os
from pprint import pprint
import json
import csv
from time import sleep

PF_KEY=os.environ["PF_KEY"]
p = Petfinder(PF_KEY)

f_pets = open('pets.json', 'w')

with open('shelter.json', 'r') as f:
    for line in f:
        pets = p.shelter_get_pets(json.loads(line)['id'], count=1000)
        for pet in pets:
            f_pets.write("{}\n".format(json.dumps(pet)))
