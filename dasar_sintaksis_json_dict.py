users = {
"id": 1,
"name": "Leanne Graham",
"username": "Bret",
"email": "Sincere@april.biz",
"address":
    {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}

print(users)
print("id :", users["id"])
print("Name :", users["name"])
print("Username :", users["username"])
print("Email : ", users["email"])
print("street : ", users["address"]["street"])
print("suite : ", users["address"]["suite"])
print("city : ", users["address"]["city"])
print("zipcode : ", users["address"]["zipcode"])
print("Lat : ", users["address"]["geo"]["lat"] )
print("Lng : ", users["address"]["geo"]["lng"])

print(type(users))
import json
print("cetak dengan json dump")
result = json.dumps(users)
print(result)
print(type(result))


print("cetak json ke file")
with open('result.json', 'w') as file:
    json.dump(users, file)
