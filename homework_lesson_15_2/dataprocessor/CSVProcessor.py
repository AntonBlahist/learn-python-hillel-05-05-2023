import datetime
import pathlib
import pandas as pd
from .file_processor import FileProcessor


class CSVProcessor(FileProcessor):
    def __init__(
            self,
            processed_filenames: list[str],
            path: str,
            date: datetime.date,
            time: datetime.time,
            sku: str,
            warehouse: str,
            warehouse_cell_id: int,
            operation: str,
            invoice: str,
            expiration_date: datetime.date,
            operation_cost: float,
            comment: str
    ):
        """
        SubClass CSVProcessor
        :param processed_filenames: filenames list
        :param path: file path
        :param date: event date
        :param time: event time
        :param sku: unique product ID
        :param warehouse: unique ID of the warehouse
        :param warehouse_cell_id: shelf number where the SKU is located
        :param operation: operation type
        :param invoice: invoice number
        :param expiration_date: date of SKU expiration
        :param operation_cost: operation cost
        (loss if less than zero, profit if more than zero)
        :param comment: comment
        """
        super().__init__(
            processed_filenames=processed_filenames,
            path=path,
            date=date,
            time=time,
            sku=sku,
            warehouse=warehouse,
            warehouse_cell_id=warehouse_cell_id,
            operation=operation,
            invoice=invoice,
            expiration_date=expiration_date,
            operation_cost=operation_cost,
            comment=comment
        )

    def process_directory(self):
        # Create a list of CSV file names.
        for entry in pathlib.Path(self.path).iterdir():
            if entry.is_file() and ".csv" in entry.name:
                self.processed_filenames.append(entry.name)
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
        for file in self.processed_filenames:
            data = pd.read_csv(self.path + file)
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
