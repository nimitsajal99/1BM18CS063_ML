import csv

a = []

with open("enjoysport.csv", 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    # print(a)

specific = []
general = []

def createG():
    G = []
    for i in range(len(a[0])-1):
        G.append("0")
    return G

for i in range(len(a[0])-1):
    specific.append("0")

# print(specific)
# print(general)

for i in range(len(a)):
    for j in range(len(a[0])-1):
        if a[i][len(a[0])-1] == "yes":
            if specific[j] == "0":
                specific[j] = a[i][j]
            elif specific[j] != a[i][j]:
                specific[j] = "?"

for i in range(len(a)):
    for j in range(len(a[0])-1):
        if a[i][len(a[0])-1] == "no":
            if specific[j] != a[i][j] and specific[j] != "?":
                temp = createG()
                temp[j] = specific[j]
                general.append(temp)

print(specific)
print("")
print(general)