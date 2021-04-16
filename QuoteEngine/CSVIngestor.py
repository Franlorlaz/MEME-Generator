"""CSVIngestor class.

Definition of CSVIngestor class, a class to read .csv files
and generate a list of QuoteModel objects from it.
"""

import pandas

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Consume .csv files to generate a list of QuoteModel objects."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate a list of QuoteModel objects from a .csv file.

        :param path: Path to a .csv file.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            ext = path.split(".")[-1]
            raise TypeError(f'Extension ".{ext}" not allowed.')

        quotes = []
        file = pandas.read_csv(path, header=0)
        for index, row in file.iterrows():
            body = row['body'].replace('"', '').strip()
            author = row['author'].replace('"', '').strip()
            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)

        return quotes
