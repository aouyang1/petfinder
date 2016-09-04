import requests

class Petfinder(object):
    def __init__(self, key):
        self.key = key
        self.endpoint = "http://api.petfinder.com/"

    def build_request(self, method, args):
        if type(args) is not dict:
            return

        arg_text = ""
        for item in args:
            print(item)
            arg_text += "".join([str(item),"=",str(args[item]),"&"])

        return self.endpoint + method + "?" + arg_text

    def remove_extra_tag(self, d):
        if not isinstance(d,dict):
            return

        for k,v in d.items():
            if isinstance(d[k],dict):
                self.remove_extra_tag(d[k])
        

    def breed_list(self, animal):
        args = {"key": self.key,
                "animal": animal,
                "format": "json"}

        req = self.build_request("breed.list", args)

        return requests.get(req).json()

    def pet_get(self, id):
        args = {"key": self.key,
                "id": id,
                "format": "json"}

        req = self.build_request("pet.get", args)

        return requests.get(req).json()

    def shelter_find(self, location, offset=0, count=25):
        args = {"key": self.key,
                "location": location,
                "offset": offset,
                "count": count,
                "format": "json"}

        req = self.build_request("shelter.find", args)

        return requests.get(req).json()

    def shelter_get_pets(self, id, status="A", offset=0, count=25, output="basic"):
        args = {"key": self.key,
                "id": id,
                "status": status,
                "offset": offset,
                "count": count,
                "output": output,
                "format": "json"}

        req = self.build_request("shelter.getPets", args)

        return requests.get(req).json()



