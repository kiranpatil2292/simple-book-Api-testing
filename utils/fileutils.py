import csv
import json

from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
print(base_dir)
test_data_dir = base_dir.joinpath('TestData')


def getjsonFromFile(filename):
    filepath = test_data_dir.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)


def getjsonFile(filename):
    filepath = test_data_dir.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)


def getCsvDataAsDict(filename):
    filepath = test_data_dir.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.DictReader(file)
        dictList = list(csvFile)
    return dictList

