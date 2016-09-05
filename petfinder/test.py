from Petfinder import Petfinder
import os
from pprint import pprint

PF_KEY=os.environ["PF_KEY"]

p = Petfinder(PF_KEY)

resp = p.shelter_find(location="94403", count=1)
pprint(resp)

blist = p.breed_list(animal="horse")
pprint(blist)

shelter = p.shelter_get_pets(id="CA690", count=1)
pprint(shelter)

pet = p.pet_get(id="11914725")
pprint(pet)
