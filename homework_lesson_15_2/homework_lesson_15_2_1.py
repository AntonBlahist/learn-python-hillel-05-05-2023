import pathlib
# from dataprocessor import DataEntry, MetricCalculator, FileProcessor


if __name__ == "__main__":
    # Create a list of files names
    files = []
    for entry in pathlib.Path("SKU/").iterdir():
        if entry.is_file():
            files.append(entry.name)
    for file in files:
        print(type(file), file)
