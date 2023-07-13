import datetime
import pathlib
import pandas as pd
from .file_processor import FileProcessor


class JSONProcessor(FileProcessor):
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
        SubClass JSONProcessor
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
        # Create a list of JSON files names.
        for entry in pathlib.Path(self.path).iterdir():
            if entry.is_file() and ".json" in entry.name:
                self.processed_filenames.append(entry.name)
        # Read JSON files.
