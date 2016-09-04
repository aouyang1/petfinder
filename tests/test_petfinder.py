import pytest
from petfinder.Petfinder import Petfinder
import os

PF_KEY=os.environ["PF_KEY"]
p = Petfinder(PF_KEY)

def test_shelter_find():
    p.shelter_find("94403")

