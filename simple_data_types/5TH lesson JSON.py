import _json
import json

json_string =
{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true
    }
  ]
}
                #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
with open('simple_data.json', 'r', encoding='utf8') as file:
    data = json.load(file)


for person in data['people']:
    if person['has_licence'] == False:
        data['people'].remove(person)

with open('sample2_copy.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2)

# works as python dictionary
