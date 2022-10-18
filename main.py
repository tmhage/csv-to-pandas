import csv

with open("TopRichestInWorld.csv") as file:
    data = csv.reader(file)
    # Print only the NetWorth column
    print(*[line[1] for line in list(data)[2:-1]])
