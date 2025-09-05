""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Mark Batac"
__version__ = "1.0.11"


from genre.genre import Genre


class LibraryItem:
    """
    Represents an item in the library.

    Attributes (private):
        __item_id (int): An id number to uniquely identify the library item.
        __title (str): The title of the library item. Cannot be blank.
        __author (str): The author of the library item. Cannot be blank.
        __genre (Genre): The genre of the library item. Must be a valid Genre.
        __is_borrowed (bool): Identifies whether the library item is borrowed (True) or available (False).
    """

    def __init__(self, item_id: int, title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Initializes a new LibraryItem instance.

        Args:
            item_id (int): An id number to uniquely identify the library item. Must be numeric.
            title (str): The title of the library item. Cannot be blank or whitespace.
            author (str): The author of the library item. Cannot be blank or whitespace.
            genre (Genre): The genre of the library item. Must be a valid Genre.
            is_borrowed (bool): True if the item is borrowed, False if it is available.

        Raises:
            ValueError: If item_id is not an integer.
            ValueError: If title is blank or whitespace.
            ValueError: If author is blank or whitespace.
            ValueError: If genre is not a valid Genre.
            ValueError: If is_borrowed is not a boolean value.
        """
        # --- item_id validation ---
        if type(item_id) is not int:  # ensures bool is not accepted
            raise ValueError("Item Id must be numeric.")
        self.__item_id = item_id

        # --- title validation ---
        if not title or not title.strip():
            raise ValueError("Title cannot be blank.")
        self.__title = title.strip()

        # --- author validation ---
        if not author or not author.strip():
            raise ValueError("Author cannot be blank.")
        self.__author = author.strip()

        # --- genre validation ---
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        self.__genre = genre

        # --- is_borrowed validation ---
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")
        self.__is_borrowed = is_borrowed

    # -------- Accessors (read-only) --------
    @property
    def item_id(self) -> int:
        """
        Returns the id number of the library item.

        Returns:
            int: The unique id of the library item.
        """
        return self.__item_id

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

    @property
    def is_borrowed(self) -> bool:
        """
        Returns the borrowed status of the library item.

        Returns:
            bool: True if the item is borrowed, False if available.
        """
        return self.__is_borrowed