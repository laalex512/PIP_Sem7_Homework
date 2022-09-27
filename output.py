from input import *


def OutputDataInConsole(key, value, path="data.csv"):
    data = InputCsvData(path)
    try:
        outputData = [line for line in data if line[key] == value]
        print(outputData)
    except:
        print("No values for this key")


def OutputDataInCsv(key, value, path="data.csv", outPath="output.csv"):
    data = InputCsvData(path)
    with open(outPath, 'w', encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(
            data[0].keys()), delimiter=' ')
        writer.writeheader()
        count = 0
        for d in data:
            if d[key] == value:
                writer.writerow(d)
                count += 1
        if count == 0:
            f.write("No values for this key")
