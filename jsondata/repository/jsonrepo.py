from jsondata.service.testdataservice import get_test_data
import os


class JsonRepository:
    def __init__(self, dataspec):
        self._length = dataspec.get("length")
        self._fields = dataspec.get("fields")

    def get_json_data(self, filename):
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'generated_files',
                                filename)
        with open(filepath, 'a') as f:
            for _ in range(self._length):
                res = {}
                for field in self._fields:
                    res[field['name']] = get_test_data(field['type'], 1)[0]
                f.write(res.__repr__() + ',\n')
        return filepath
