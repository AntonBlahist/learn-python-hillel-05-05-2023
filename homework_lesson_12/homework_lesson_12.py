import csv
import os


def open_csv_file(filename):
    """
    The function reads the CSV file and prints every row.
    """
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)


def get_unique_id(filename):
    """
    The function creates a unique ID for every row in the CSV file.
    """
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        unique_id_dict = {}
        i = 1
        for row in reader:
            unique_id_dict[i] = row
            i += 1
        return unique_id_dict


def get_category_brand_id(unique_id_dict: dict, category, brand: tuple):
    """
    The function creates a dictionary
    in which keys are a tuple (category, brand)
    and values are a list of unique IDs
    which have corresponding values in the category and brand fields.
    """
    category_brand_tuple = (category, brand)
    # if category in dict.keys():


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
    ids_dict = get_unique_id("tech_inventory.csv")
    for key, value in ids_dict.items():
        print(key, ":", value)
