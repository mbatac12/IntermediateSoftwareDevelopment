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

    # 1) Create a LibraryItem instance with VALID inputs (uses new arg list)
    try:
        
        item1 = LibraryItem(101, "The Great Gatsby", "F. Scott Fitzgerald", Genre.FICTION, False)
        print("LibraryItem created successfully!")
    except ValueError as e:
        print(f"Error: {e}")

    # 2) Print attributes using accessors
    try:
        print(f"ID: {item1.item_id}")
        print(f"Title: {item1.title}")
        print(f"Author: {item1.author}")
        print(f"Genre: {item1.genre.name}")   # .name shows "FICTION"
        print(f"Borrowed: {item1.is_borrowed}")
    except Exception as e:
        print(f"Error accessing attributes: {e}")

    print("\n--- Testing Invalid Inputs ---")

    # 3a) Blank title
    try:
        LibraryItem(102, "", "George Orwell", Genre.FICTION, False)
    except ValueError as e:
        print(f"Error: {e}")

    # 3b) Blank author
    try:
        LibraryItem(103, "1984", "", Genre.FICTION, False)
    except ValueError as e:
        print(f"Error: {e}")

    # 3c) Invalid genre (not a Genre enum)
    try:
        LibraryItem(104, "The Hobbit", "J.R.R. Tolkien", "Adventure", False)
    except ValueError as e:
        print(f"Error: {e}")

    # 3d) Invalid item_id (must be numeric int)
    try:
        LibraryItem("105", "Brave New World", "Aldous Huxley", Genre.FICTION, False)
    except ValueError as e:
        print(f"Error: {e}")

    # 3e) Invalid is_borrowed (must be boolean)
    try:
        LibraryItem(106, "Animal Farm", "George Orwell", Genre.FICTION, "Yes")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()