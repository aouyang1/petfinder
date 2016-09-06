from Petfinder import Petfinder
import os
from pprint import pprint
import json
import csv
from time import sleep

PF_KEY=os.environ["PF_KEY"]
p = Petfinder(PF_KEY)

part="al"

f_pets = open('pets-{}.json'.format(part), 'w')

with open('part-{}'.format(part), 'r') as f:
    for line in f:
        shelter_id = json.loads(line)['id']
        try:
            print("fetching pets from shelder id: {}".format(shelter_id))
            pets = p.shelter_get_pets(shelter_id, count=1000)
            for pet in pets:
                f_pets.write("{}\n".format(json.dumps(pet)))
        except:
            print("could not fetch pets from shelter id: {}".format(shelter_id))
