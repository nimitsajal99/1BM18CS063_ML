import csv

a = []

with open("sample.csv", 'r') as csvfile:
	for row in csv.reader(csvfile):
		a.append(row)
	print a

ans = []

for i in range(len(a[0])):
	ans.append("0")

#print(ans)

for i in range(len(a)):
	for j in range(len(a[0])):
		if a[i][len(a[0])-1] == "yes":
			if ans[j] == "0":
				ans[j] = a[i][j]
			elif ans[j] != a[i][j]:
				ans[j] = "?"
	#print(ans)

print("")	

print(ans)
