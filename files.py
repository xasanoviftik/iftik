with open("text.txt", "r") as file:
    file = file.readlines()

result = dict()
first_row = file[:1]
first_row = first_row[0].split("\t")
for i in first_row[3:]:
    result[i] = ["", 0]


for line in file[1:]:
    row = line.split("\t")
    
    print(row)
print()
print(first_row)
