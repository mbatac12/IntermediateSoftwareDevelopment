""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Mark Batac"
__version__ = "1.0.11"

from genre.genre import Genre

class LibraryItem:
    """
    Represents an item in the library.

    Attributes:
        __title (str): The title of the library item. Cannot be blank.
        __author (str): The author of the library item. Cannot be blank.
        __genre (Genre): The genre of the library item. Must be a valid Genre.
    """

    def __init__(self, title: str, author: str, genre: Genre):
        """
        Initializes a new LibraryItem instance.

        Args:
            title (str): The title of the library item. Cannot be blank.
            author (str): The author of the library item. Cannot be blank.
            genre (Genre): The genre of the library item. Must be a valid Genre.

        Raises:
            ValueError: If title is blank.
            ValueError: If author is blank.
            ValueError: If genre is not a valid Genre.
        """
        # --- Title validation ---
        if not title or not title.strip():
            raise ValueError("Title cannot be blank.")
        self.__title = title.strip()

        # --- Author validation ---
        if not author or not author.strip():
            raise ValueError("Author cannot be blank.")
        self.__author = author.strip()

        # --- Genre validation ---
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        self.__genre = genre

    @property
    def title(self) -> str:
        """
        Returns the title of the library item.

        Returns:
            str: The title of the library item.
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        Returns the author of the library item.

        Returns:
            str: The author of the library item.
        """
        return self.__author

    @property
    def genre(self) -> Genre:
        """
        Returns the genre of the library item.

        Returns:
            Genre: The genre of the library item.
        """
        return self.__genre