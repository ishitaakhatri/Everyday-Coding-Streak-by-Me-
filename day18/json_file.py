import json
people_string = '''
{
    "people": [
        {
            "name":"john smith",
            "phone":"615-555-7164",
            "email":"john.smith@work-place.com",
            "has_licence":false
        },
        {
            "name":"jane doe",
            "phone":"560-777-8915",
            "email":"jane.doe@work-place.com",
            "has_licence":true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)
for person in data['people']:
    del person['phone']

new_string = json.dumps(data,indent=2,sort_keys=True)
print(new_string)