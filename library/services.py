from datetime import datetime
from sqlalchemy import or_, not_
from .models import Author,Book
from .db import get_db



# AUTHOR CRUD
def create_author(name: str, bio: str = None) -> Author:
    """Yangi muallif yaratish"""
    author = Author(
        name = name,
        bio = bio,
    )
    
    with get_db() as session:
        session.add(author)
        session.commit()

def get_author_by_id(author_id: int) -> Author | None:
    """ID bo'yicha muallifni olish"""
    pass

def get_all_authors() -> list[Author]:
    """Barcha mualliflar ro'yxatini olish"""
    pass

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    pass

def delete_author(author_id: int) -> bool:
    """Muallifni o'chirish (faqat kitoblari bo'lmagan holda)"""
    pass


# BOOK CRUD

def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    """Yangi kitob yaratish"""
    book = Book(
        title = title,
        author_id = author_id,
        published_year = published_year,
        isbn = isbn
    )

    with get_db() as session:
        session.add(book)
        session.commit()
        

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    pass

def get_all_books() -> list[Book]:
    """Barcha kitoblar ro'yxatini olish"""
    pass

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni sarlavha bo'yicha qidirish (partial match)"""
    pass

def delete_book(book_id: int) -> bool:
    """Kitobni o'chirish"""
    pass
