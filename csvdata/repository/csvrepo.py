import os
import pandas as pd

from commons.service.testdataservice import get_test_data


class CsvRepository:
    def __init__(self, dataspec):
        self._length = dataspec.get("length")
        self._fields = dataspec.get("fields")

    def get_csv_data(self, filename):
        import time
        print(time.strftime("%H:%M:%S"))
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'generated_files',
                                filename + '.csv')
        df = pd.DataFrame(columns=[field['name'] for field in self._fields])
        df.to_csv(filepath, header=True, index=False, mode='w')
        batch_size = 30000
        batch_count = int(self._length / batch_size)
        remainder_row_count = self._length % batch_size
        for _ in range(batch_count):
            self._insert_csv_rows(filepath, batch_size)
        self._insert_csv_rows(filepath, remainder_row_count)
        print(time.strftime("%H:%M:%S"))
        return filepath

    def _insert_csv_rows(self, filepath, count):
        df = pd.DataFrame(columns=[field['name'] for field in self._fields])
        for field in self._fields:
            df[field['name']] = [get_test_data(field['type']).replace('\n', ' ').replace(',', '')
                                 for _ in range(count)]
        df.to_csv(filepath, header=False, index=False, mode='a')
