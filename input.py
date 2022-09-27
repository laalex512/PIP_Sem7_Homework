import csv
from keys import keys

def InputTxtData(path):
    with open(path, "r", encoding="UTF-8") as f:
        temp = f.read().split("\n")
    data = []
    for line in temp:
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = line.split()[i]
        data.append(dict)
    return data


def InputCsvData(path):
    with open(path, encoding="UTF-8") as f:
        data = list(csv.DictReader(f, delimiter=' '))
    return data