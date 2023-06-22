import csv
import os


def open_csv_file(filename):
    """
    The function reads the CSV file and prints every row.
    """
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    if not os.path.isfile("tech_inventory.csv"):
        print("The program won't start without tech_inventory.csv.")
        exit(-1)
    open_csv_file("tech_inventory.csv")
