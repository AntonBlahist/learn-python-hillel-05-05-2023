import datetime
import pathlib
import pandas as pd
import uuid


class FileProcessor:
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
        SuperClass FileProcessor
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
        self.processed_filenames = processed_filenames
        self.path = path
        self.date = date
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment

    def process_directory(self):
        pass


class JSONProcessor(FileProcessor):
    def __init__(
            self,
            processed_filenames: list[str],
            path: str
    ):
        """
        SubClass JSONProcessor
        """
        super().__init__(
            processed_filenames=processed_filenames,
            path=path
        )

    def process_directory(self):
        # Create a list of files names
        for entry in pathlib.Path(self.path).iterdir():
            if entry.is_file():
                self.processed_filenames.append(entry.name)


class CSVProcessor(FileProcessor):
    def __init__(
            self,
            processed_filenames: list[str],
            path: str
    ):
        """
        SubClass CSVProcessor
        """
        super().__init__(
            processed_filenames=processed_filenames,
            path=path
        )

    def process_directory(self):
        # Create a list of files names
        for entry in pathlib.Path(self.path).iterdir():
            if entry.is_file():
                self.processed_filenames.append(entry.name)
