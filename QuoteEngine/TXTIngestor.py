"""TXTIngestor class.

Definition of TXTIngestor class, a class to read .txt files
and generate a list of QuoteModel objects from it.
"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Consume .txt files to generate a list of QuoteModel objects."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate a list of QuoteModel objects from a .txt file.

        :param path: Path to a .txt file.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            ext = path.split(".")[-1]
            raise TypeError(f'Extension ".{ext}" not allowed.')

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as file:
            for line in file.readlines():
                line = line.split(' - ')
                body = line[0].replace('"', '').strip()
                author = line[1].replace('"', '').strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
