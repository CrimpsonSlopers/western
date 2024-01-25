import json

with open("auction.json", "r") as f:
    data = json.load(f)

newData = []

for d in data:
    newData.append(
        {
            "slug": int(d["slug"]),
            "name": d["name"],
            "fullName": d["full_name"],
            "reportDate": "2023-08-01T00:00:00.000Z",
            "publishedDate": "2023-08-01T00:00:00.000Z",
            "marketType": d["market"],
        }
    )


with open("d.json", "w") as f:
    json.dump(newData, f)
