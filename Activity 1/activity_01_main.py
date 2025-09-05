""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.4"
__credits__ = "Mark Batac"


from library_item.library_item import LibraryItem
from genre.genre import Genre


def main():
    """
    Test the functionality of the methods encapsulated in this project.
    """
    print("=== LibraryItem Client Program ===\n")

    # 1. Create a LibraryItem instance with valid inputs
    try:
        item1 = LibraryItem("The Great Gatsby", "F. Scott Fitzgerald", Genre.FICTION)
        print("LibraryItem created successfully!")
    except ValueError as e:
        print(f"Error: {e}")

    # 2. Print attributes using accessors
    try:
        print(f"Title: {item1.title}")
        print(f"Author: {item1.author}")
        print(f"Genre: {item1.genre.name}")  # .name shows "FICTION"
    except Exception as e:
        print(f"Error accessing attributes: {e}")

    print("\n--- Testing Invalid Inputs ---")

    # 3a. Create a LibraryItem with a blank title
    try:
        item2 = LibraryItem("", "George Orwell", Genre.FICTION)
    except ValueError as e:
        print(f"Error: {e}")

    # 3b. Create a LibraryItem with a blank author
    try:
        item3 = LibraryItem("1984", "", Genre.FICTION)
    except ValueError as e:
        print(f"Error: {e}")

    # 3c. Create a LibraryItem with an invalid genre
    try:
        item4 = LibraryItem("The Hobbit", "J.R.R. Tolkien", "Adventure")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
