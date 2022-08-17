from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    with open(path) as file:
        csv_file = csv.DictReader(file)
        result = []
        for row in csv_file:
            result.append(row)
    return result
