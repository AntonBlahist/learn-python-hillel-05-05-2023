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


def get_unique_id():
    """
    The function creates a unique ID for every row in the CSV file.
    """
    pass


def get_category_id():
    """
    The function creates a category ID and prints a list of unique IDs
    that have this value in the category field.
    """
    pass


def get_brand_id():
    """
    The function creates a category ID and prints a list of unique IDs
    that have this value in the brand field.
    """
    pass


def get_product_quantity():
    """
    The function prints how many items there are
    from each brand and in each category.
    """
    pass  # Use brand and category IDs


def get_product_info():
    """
    The function prints a full info of each product
    for a specified brand or category.
    """
    pass


def get_brand_quantity():
    """
    The function prints the number of items by brand for each category.
    """
    pass


if __name__ == "__main__":
    if not os.path.isfile("tech_inventory.csv"):
        print("The program won't start without tech_inventory.csv.")
        exit(-1)
    open_csv_file("tech_inventory.csv")
