import requests
import json
import jsonpath


url  = "https://swapi.co/api/people/"

class fetchData():
    def data(self):
        request = requests.get(url)
        response = json.loads(request.text)
        person = jsonpath.jsonpath(response,"results")
        listName = []
        for i in person[0]:
            listName.append(i['name'])

        return listName