import os
from enum import Enum

import pandas as pd

STORAGE_FOLDER = os.path.dirname(__file__)


class FileTypes(Enum):
    CSV_FILE = 'csv'
    EXCEL_FILE = 'xlsx'
    H5_FILE = 'h5'
    JSON_FILE = 'json'


class CompileDataFrame:
    def __init__(self, data_frame: pd.DataFrame, filename: str):
        self.data_frame = data_frame
        self.filename = filename

    @staticmethod
    def _create_csv(data_frame: pd.DataFrame, filename: str) -> str:
        filepath = os.path.join(STORAGE_FOLDER, filename + ".csv")
        data_frame.to_csv(filepath)
        return filepath

    @staticmethod
    def _create_excel(data_frame: pd.DataFrame, filename: str) -> str:
        filepath = os.path.join(STORAGE_FOLDER, filename + ".xlsx")
        data_frame.to_excel(filepath)
        return filepath

    @staticmethod
    def _create_hdf(data_frame: pd.DataFrame, filename: str, key: str) -> str:
        filepath = os.path.join(STORAGE_FOLDER, filename + ".h5")
        data_frame.to_hdf(filepath, key, mode="w")
        return filepath

    @staticmethod
    def _create_json(data_frame: pd.DataFrame, filename: str) -> str:
        filepath = os.path.join(STORAGE_FOLDER, filename + ".json")
        data_frame.to_json(filepath)
        return filepath

    def create_file(self, file_type: FileTypes, key: str = 'my_data') -> str:
        """
        Создает файл заданного типа (csv, excel, hdf, json) и возвращает путь к созданному файлу.

        :param
            file_type (FileTypes): Тип файла для создания.
            key (str, optional): Аргумент для HDF файлов. Используется в методе `to_hdf`.

        :return
            str: Путь к созданному файлу.
        """

        print(('=' * 10) + f'Пишем файл ({str(file_type)}) ...')
        try:
            if file_type == FileTypes.CSV_FILE:
                return self._create_csv(self.data_frame, self.filename)
            elif file_type == FileTypes.EXCEL_FILE:
                return self._create_excel(self.data_frame, self.filename)
            elif file_type == FileTypes.H5_FILE:
                if key is None:
                    raise ValueError("Argument 'key' is required for HDF files.")
                return self._create_hdf(self.data_frame, self.filename, key)
            elif file_type == FileTypes.JSON_FILE:
                return self._create_json(self.data_frame, self.filename)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
        except Exception as e:
            is_exception = True
            print(f'Ошибка при записи файла\nError: {e}')
