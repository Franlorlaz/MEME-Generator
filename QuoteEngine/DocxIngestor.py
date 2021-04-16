"""DocxIngestor class.

Definition of DocxIngestor class, a class to read .docx files
and generate a list of QuoteModel objects from it.
"""

import docx

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Consume .docx files to generate a list of QuoteModel objects."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate a list of QuoteModel objects from a .docx file.

        :param path: Path to a .docx file.
        :return: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            ext = path.split(".")[-1]
            raise TypeError(f'Extension ".{ext}" not allowed.')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split('-')
                body = parse[0].replace('"', '').strip()
                author = parse[1].replace('"', '').strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
