from input import *
from keys import keys
import csv


def WriteInCsv(data, path="data.csv"):
    with open(path, 'a', encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(
            data[0].keys()), delimiter=' ')
        try:
            if InputCsvData(path)[0] == 0:
                writer.writeheader()
        except:
            writer.writeheader()
        for d in OnlyNewInCsv(data):
            writer.writerow(d)


def OnlyNewInCsv(data, path="data.csv"):
    alreadyExist = InputCsvData(path)
    return [d for d in data if d not in alreadyExist]
