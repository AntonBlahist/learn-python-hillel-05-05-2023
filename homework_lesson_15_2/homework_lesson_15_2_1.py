import pathlib
# from dataprocessor import DataEntry, MetricCalculator, FileProcessor


if __name__ == "__main__":
    # Create a list of files objects
    files = []
    for entry in pathlib.Path("SKU/").iterdir():
        if entry.is_file():
            files.append(entry)
