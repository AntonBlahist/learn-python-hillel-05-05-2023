import datetime
import pathlib


class DataEntry:
    def __init__(
            self,
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
        Class DataEntry
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

    def expired(self):
        """
        The method is responsible
        for showing how many unique SKUs were lost
        (expiration_date passed and the sale didn't take place)
        :return:
        """
        pass
