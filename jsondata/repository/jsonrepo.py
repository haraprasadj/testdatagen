import os
import pandas as pd
from commons.service.testdataservice import get_test_data


class JsonRepository:
    def __init__(self, dataspec):
        self._length = dataspec.get("length")
        self._fields = dataspec.get("fields")

    def get_json_data(self, filename):
        import time
        print(time.strftime("%H:%M:%S"))
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'generated_files',
                                filename + '.json')
        df = pd.DataFrame(columns=[field['name'] for field in self._fields])
        for field in self._fields:
            df[field['name']] = [get_test_data(field['type']) for _ in range(self._length)]
        with open(filepath, 'a') as f:
            f.write(df.to_json(orient='records'))
        print(time.strftime("%H:%M:%S"))
        return filepath
