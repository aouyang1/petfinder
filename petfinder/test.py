from Petfinder import Petfinder
import os
from pprint import pprint

PF_KEY=os.environ["PF_KEY"]

p = Petfinder(PF_KEY)

pprint(p.shelter_find("94403"))
