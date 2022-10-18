import csv
import locale

locale.setlocale(locale.LC_ALL, '')

with open("TopRichestInWorld.csv") as file:
    data = csv.reader(file)
    # Print only the NetWorth column
    networths = [line[1] for line in list(data)[2:]]

# Extract float value from string NetWorth column
converted = [locale.atof(val.strip('$')) for val in networths]
