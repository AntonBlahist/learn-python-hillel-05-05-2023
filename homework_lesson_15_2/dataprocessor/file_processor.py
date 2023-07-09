import pandas as pd
import uuid


class FileProcessor:
    def __init__(
            self,
            processed_filenames: list[str],
            data: list[DataEntry],  # don't know what is expected here yet
            # additional parameter expected
    ):
        """
        SuperClass FileProcessor
        :param processed_filenames: file list
        :param data:
        """
        self.processed_filenames = processed_filenames
        self.data = data
        # additional variable expected

    def process_directory(self):  # additional parameter expected
        pass


class JSONProcessor(FileProcessor):
    def __init__(
            self,
            processed_filenames: list[str],
            data: list[DataEntry],  # don't know what is expected here yet
            # additional parameter expected
    ):
        """
        SubClass JSONProcessor
        :param processed_filenames:
        :param data:
        """
        super().__init__(
            processed_filenames=processed_filenames,
            data=data,
            # additional parameter expected
        )

    def process_directory(self):  # additional parameter expected
        pass


class CSVProcessor(FileProcessor):
    def __init__(
            self,
            processed_filenames: list[str],
            data: list[DataEntry],  # don't know what is expected here yet
            # additional parameter expected
    ):
        """
        SubClass CSVProcessor
        :param processed_filenames:
        :param data:
        """
        super().__init__(
            processed_filenames=processed_filenames,
            data=data,
            # additional parameter expected
        )

    def process_directory(self):  # additional parameter expected
        pass
