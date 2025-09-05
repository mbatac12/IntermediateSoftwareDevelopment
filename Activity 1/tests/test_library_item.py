"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Mark Batac"
__version__ = "1.0.8"

import unittest

from library_item.library_item import LibraryItem
from genre.genre import Genre


class TestLibraryItem(unittest.TestCase):
    # ---------- __init__ ----------
    # Test Case 1
    def test_init_sets_input_values(self):
        """Test #1: Ensure attributes are set to input values"""
        # Arrange
        title = "Harry Potter"
        author = "J.K. Rowling"
        genre = Genre.FICTION

        # Act
        item = LibraryItem(title, author, genre)

        # Assert
        self.assertEqual(item._LibraryItem__title, title)
        self.assertEqual(item._LibraryItem__author, author)
        self.assertEqual(item._LibraryItem__genre, genre)

    # Test Case 2
    def test_init_blank_title_raises_exception(self):
        """Test #2: Exception raised when title is blank"""
        with self.assertRaisesRegex(ValueError, "Title cannot be blank."):
            LibraryItem("", "J.K. Rowling", Genre.FICTION)

        with self.assertRaisesRegex(ValueError, "Title cannot be blank."):
            LibraryItem("   \t", "J.K. Rowling", Genre.FICTION)

    # Test Case 3
    def test_init_blank_author_raises_exception(self):
        """Test #3: Exception raised when author is blank"""
        with self.assertRaisesRegex(ValueError, "Author cannot be blank."):
            LibraryItem("Harry Potter", "", Genre.FICTION)

        with self.assertRaisesRegex(ValueError, "Author cannot be blank."):
            LibraryItem("Harry Potter", "   ", Genre.FICTION)

    # Test Case 4
    def test_init_invalid_genre_raises_exception(self):
        """Test #4: Exception raised when invalid Genre"""
        with self.assertRaisesRegex(ValueError, "Invalid Genre."):
            LibraryItem("Harry Potter", "J.K. Rowling", "Adventure")  # not a Genre

    # ---------- Accessors ----------
    # Test Case 5
    def test_title_returns_title_attribute(self):
        """Test #5: title property returns title attribute"""
        item = LibraryItem("Harry Potter", "J.K. Rowling", Genre.FICTION)
        self.assertEqual(item.title, "Harry Potter")

    # Test Case 6
    def test_author_returns_author_attribute(self):
        """Test #6: author property returns author attribute"""
        item = LibraryItem("Harry Potter", "J.K. Rowling", Genre.FICTION)
        self.assertEqual(item.author, "J.K. Rowling")

    # Test Case 7
    def test_genre_returns_genre_attribute(self):
        """Test #7: genre property returns genre attribute"""
        item = LibraryItem("Harry Potter", "J.K. Rowling", Genre.FICTION)
        self.assertEqual(item.genre, Genre.FICTION)


if __name__ == "__main__":
    unittest.main()