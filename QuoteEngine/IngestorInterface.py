"""IngestorInterface abstract class.

IngestorInterface define the base scheme
to every file importer of this module.
"""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class defining file importer scheme."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Compute if the file extension is allowed."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate a list of QuoteModel objects from a file."""
        pass
