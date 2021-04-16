"""Ingestor class.

Definition of a usefull class to generate a list of QuoteModel objects
based on data from different file types.
"""

from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Consume files to generate a list of QuoteModel objects."""

    ingestors = [TXTIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate a list of QuoteModel objects from a file.

        :param path: Path to a file.
        :return: A list of QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        ext = path.split(".")[-1]
        raise TypeError(f'Extension ".{ext}" not allowed.')
