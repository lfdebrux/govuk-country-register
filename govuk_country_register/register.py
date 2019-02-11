
import csv
from pathlib import Path

class Register:

    __metadata_keys__ = [
        "index-entry-number",
        "entry-number",
        "entry-timestamp",
        "key",
        "start-date",
        "end-date",
    ]

    def find(self, key):
        """Find a record using the register key"""

        return self.data[key]["item"]

    @classmethod
    def from_csv(cls, path):
        """Read a register CSV file

        :param os.PathLike path:  path to the CSV file
        """

        data = {}
        with open(path, newline="") as f:
            for record in csv.DictReader(f):
                key = record["key"]
                metadata = {k: v for k, v in record.items() if k in cls.__metadata_keys__}
                item = {k: v for k, v in record.items() if k not in cls.__metadata_keys__}
                data[key] = metadata.copy()
                data[key]["item"] = item.copy()

        register = cls.__new__(cls)
        register.data = data

        return register
