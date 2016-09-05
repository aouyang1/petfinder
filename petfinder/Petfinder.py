import requests

class Petfinder(object):
    def __init__(self, key):
        self.key = key
        self.endpoint = "http://api.petfinder.com/"

    def remove_extra_tag(self, d):
        if not isinstance(d, dict):
            if isinstance(d, list):
                for item in d:
                    self.remove_extra_tag(item)
            return

        for k,v in d.items():
            # check if current key holds a dict containing $t as a key
            if isinstance(d[k], dict) and "$t" in d[k]:
                d[k] = d[k]["$t"]

            # check if list is composed of dicts with $t as a key
            if isinstance(d[k], list) and len(d[k])>0 and "$t" in d[k][0]:
                d[k] = list(map(lambda x: x["$t"], d[k]))

            # continue searching into json payload
            self.remove_extra_tag(d[k])

    def breed_list(self, animal):
        args = {"key": self.key,
                "animal": animal,
                "format": "json"}

        api_endpoint = "".join([self.endpoint, "breed.list"])

        resp = requests.get(api_endpoint, params=args).json()
        self.remove_extra_tag(resp)

        return resp['petfinder']['breeds']['breed']

    def pet_get(self, id):
        args = {"key": self.key,
                "id": id,
                "format": "json"}

        api_endpoint = "".join([self.endpoint, "pet.get"])

        resp = requests.get(api_endpoint, params=args).json()
        self.remove_extra_tag(resp)

        return resp['petfinder']['pet']

    def shelter_find(self, location, offset=0, count=25):
        args = {"key": self.key,
                "location": location,
                "offset": offset,
                "count": count,
                "format": "json"}

        api_endpoint = "".join([self.endpoint, "shelter.find"])

        resp = requests.get(api_endpoint, params=args).json()
        self.remove_extra_tag(resp)

        output = resp['petfinder']['shelters']['shelter']

        return output if isinstance(output, list) else [output]

    def shelter_get_pets(self, id, status="A", offset=0, count=25, output="basic"):
        args = {"key": self.key,
                "id": id,
                "status": status,
                "offset": offset,
                "count": count,
                "output": output,
                "format": "json"}

        api_endpoint = "".join([self.endpoint, "shelter.getPets"])

        resp = requests.get(api_endpoint, params=args).json()
        self.remove_extra_tag(resp)

        output = resp['petfinder']['pets']['pet']

        return output if isinstance(output, list) else [output]



