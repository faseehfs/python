import os
import csv

FILEPATH = "file.csv"

rows = [["John", 20], ["David", 31], ["Eddie", 25]]

with open(FILEPATH, "w", newline="") as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(["name", "age"])
    csv_writer.writerows(rows)

with open(FILEPATH, "r", newline="") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        print(f"Reading line {csv_reader.line_num}.")
        print(row)

input("Press Enter to delete the CSV file.")
os.remove(FILEPATH)
