from jsondata.service.testdataservice import get_test_data
import os
import json


class JsonRepository:
    def __init__(self, dataspec):
        self._length = dataspec.get("length")
        self._fields = dataspec.get("fields")

    def get_json_data(self, filename):
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'generated_files',
                                filename + '.json')
        with open(filepath, 'a') as f:
            f.write('[')
            for _ in range(self._length - 1):
                f.write(self._get_json_item() + ',')
            f.write(self._get_json_item())
            f.write(']')
        return filepath

    def _get_json_item(self):
        res = {}
        for field in self._fields:
            res[field['name']] = get_test_data(field['type'], 1)[0]
        return json.dumps(res)
