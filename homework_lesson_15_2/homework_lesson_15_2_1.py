import pathlib
from dataprocessor import MetricCalculator, FileProcessor


if __name__ == "__main__":
    # Create a list of files names
    files = []
    path = "SKU/"
    for entry in pathlib.Path(path).iterdir():
        if entry.is_file():
            files.append(entry.name)
    for file in files:
        print(file)

"""
через self можно задавать значения параметрам класса извне (из прочитанных файлов)
таким образом, из csv и json файлов забираем нужные поля в нужные параметры,
а потом передаем их в класс DataEntry, приводя данные из разных форматов файлов 
в один формат данных
и уже потом считаем метрику
"""
