"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Mark Batac"
__version__ = "1.1.2"

import unittest

from library_item.library_item import LibraryItem
from genre.genre import Genre


class TestLibraryItem(unittest.TestCase):
       # ---------- __init__ ----------
    # Test Case 1
    def test_init_sets_input_values(self):
        """
        Test #1:
        Verify that a valid LibraryItem object is created successfully
        and all attributes are set correctly.
        """
        item = LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, False)
        self.assertEqual(item.item_id, 101)
        self.assertEqual(item.title, "Harry Potter")
        self.assertEqual(item.author, "J.K. Rowling")
        self.assertEqual(item.genre, Genre.FICTION)
        self.assertFalse(item.is_borrowed)

    # Test Case 2
    def test_init_blank_title_raises_exception(self):
        """
        Test #2:
        Verify that creating a LibraryItem with a blank title
        raises ValueError with correct message.
        """
        with self.assertRaisesRegex(ValueError, "Title cannot be blank."):
            LibraryItem(101, "", "J.K. Rowling", Genre.FICTION, False)

    # Test Case 3
    def test_init_blank_author_raises_exception(self):
        """
        Test #3:
        Verify that creating a LibraryItem with a blank author
        raises ValueError with correct message.
        """
        with self.assertRaisesRegex(ValueError, "Author cannot be blank."):
            LibraryItem(101, "Harry Potter", "", Genre.FICTION, False)

    # Test Case 4
    def test_init_invalid_genre_raises_exception(self):
        """
        Test #4:
        Verify that creating a LibraryItem with an invalid genre
        raises ValueError with correct message.
        """
        with self.assertRaisesRegex(ValueError, "Invalid Genre."):
            LibraryItem(101, "Harry Potter", "J.K. Rowling", "Adventure", False)

    # ---------- Accessors ----------
    # Test Case 5
    def test_title_returns_title_attribute(self):
        """
        Test #5:
        Verify that the title property returns the title string.
        """
        item = LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, False)
        self.assertEqual(item.title, "Harry Potter")

    # Test Case 6
    def test_author_returns_author_attribute(self):
        """
        Test #6:
        Verify that the author property returns the author string.
        """
        item = LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, False)
        self.assertEqual(item.author, "J.K. Rowling")

    # Test Case 7
    def test_genre_returns_genre_attribute(self):
        """
        Test #7:
        Verify that the genre property returns the Genre enum value.
        """
        item = LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, False)
        self.assertEqual(item.genre, Genre.FICTION)


    # ---------- New Tests (Part 2) ----------
    # Test Case 8
    def test_init_invalid_item_id_raises_exception(self):
        """
        Test #8:
        Verify that a non-numeric item_id raises ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Item Id must be numeric."):
            LibraryItem("101", "Harry Potter", "J.K. Rowling", Genre.FICTION, False)

    # Test Case 9
    def test_init_invalid_is_borrowed_raises_exception(self):
        """
        Test #9:
        Verify that a non-boolean is_borrowed raises ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Is Borrowed must be a boolean value."):
            LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, "Yes")

    # Test Case 10
    def test_item_id_returns_id_attribute(self):
        """
        Test #10:
        Verify that the item_id property returns the numeric id.
        """
        item = LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, False)
        self.assertEqual(item.item_id, 101)

    # Test Case 11
    def test_is_borrowed_returns_flag(self):
        """
        Test #11:
        Verify that the is_borrowed property returns the correct boolean flag.
        """
        item = LibraryItem(101, "Harry Potter", "J.K. Rowling", Genre.FICTION, True)
        self.assertTrue(item.is_borrowed)


if __name__ == "__main__":
    unittest.main()