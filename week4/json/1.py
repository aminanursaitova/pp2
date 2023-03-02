import json
import tabulate
x = open("C:/Users/amina/Documents/coding/pp2/week4/json/sd.json")
y = json.load(x)
a = {}
for i in range (18):
    a[i] = (dict(DN = str(y["imdata"][i]["l1PhysIf"]["attributes"]["dn"]), Description = y["imdata"][i]["l1PhysIf"]["attributes"]["descr"], Speed = y["imdata"][i]["l1PhysIf"]["attributes"]["speed"], MTU = y["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]))

headers = ["DN", "Description", "Speed", "MTU"]

table = []

for key, value in a.items():
    row = []
    for header in headers:
        row.append(value.get(header, ''))
    table.append(row)

print(tabulate.tabulate(table, headers=headers))
x.close()