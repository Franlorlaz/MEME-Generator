"""PDFIngestor class.

Definition of PDFIngestor class, a class to read .pdf files
and generate a list of QuoteModel objects from it.
"""

import os
import subprocess

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Consume .pdf files to generate a list of QuoteModel objects."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate a list of QuoteModel objects from a .pdf file.

        :param path: Path to a .pdf file.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            ext = path.split(".")[-1]
            raise TypeError(f'Extension ".{ext}" not allowed.')

        tmp = 'tmp_pdf2txt.txt'
        subprocess.run(['pdftotext', '-enc', 'UTF-8', path, tmp])

        quotes = []
        with open(tmp, 'r', encoding='utf-8-sig') as file:
            for line in file.readlines():
                line = line.split(' - ')
                if len(line) != 2:
                    continue
                body = line[0].replace('"', '').strip()
                author = line[1].replace('"', '').strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        os.remove(tmp)
        return quotes
