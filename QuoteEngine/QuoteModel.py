"""Simple QuoteModel class.

A simple class to encapsulate the body and author of a quote.
"""


class QuoteModel:
    """Simple QuoteModel class.

    A simple class to encapsulate the body and author of a quote.
    """

    def __init__(self, body, author):
        """Initialize the object with a body and an author."""
        self.body = str(body)
        self.author = str(author)

    def __str__(self):
        """Return a human-readable string representation."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """Return an object representation to debug."""
        return f'QuoteModel(body="{self.body}", author="{self.author}")'
