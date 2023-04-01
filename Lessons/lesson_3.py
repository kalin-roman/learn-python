s = {"Kiyv","Lviv","Odessa",(0,1)}
s.add("Dnepr")
s.add("Kiyv")
s.add((1,0))

for i in s:
    print(i)

s = { "Kiyv": 2757, "Lviv": 241, "Odessa": 534 }
s["Kiyv"] = 4543
s["Dnepr"] = 352

print(*s)
for key in s:
    print(key,s[key])

d = [{
        "firstName": 'Max',
        "lastName": "Kalin",
        "age": 44
    },
    {
        "firstName": 'Roma',
        "lastName": "Kalin",
        "age": 17
    }
    ]
for user in d:
    print(user["firstName"], user["lastName"], user["age"])