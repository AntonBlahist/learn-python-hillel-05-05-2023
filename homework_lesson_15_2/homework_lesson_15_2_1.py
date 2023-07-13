import pathlib
import pandas as pd
# from dataprocessor import MetricCalculator, FileProcessor, JSONProcessor, \
#     CSVProcessor


if __name__ == "__main__":
    # Check the code of a CSVProcessor method (process_directory)
    # Create a list of files names.
    csv_files = []
    path = "SKU/"
    for entry in pathlib.Path(path).iterdir():
        if entry.is_file() and ".csv" in entry.name:
            csv_files.append(entry.name)
    # Read CSV files and extract data.
    date_list = []
    time_list = []
    sku_list = []
    warehouse_list = []
    warehouse_cell_id_list = []
    operation_list = []
    invoice_list = []
    expiration_date_list = []
    operation_cost_list = []
    comment_list = []
    for file in csv_files:
        data = pd.read_csv(pathlib.Path(path + file))
        date_list.extend(data["date"].tolist())
        time_list.extend(data["time"].tolist())
        sku_list.extend(data["sku"].tolist())
        warehouse_list.extend(data["warehouse"].tolist())
        warehouse_cell_id_list.extend(data["warehouse_cell_id"].tolist())
        operation_list.extend(data["operation"].tolist())
        invoice_list.extend(data["invoice"].tolist())
        expiration_date_list.extend(data["expiration_date"].tolist())
        operation_cost_list.extend(data["operation_cost"].tolist())
        comment_list.extend(data["comment"].tolist())
    print(sku_list)
