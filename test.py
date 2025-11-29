from datetime import datetime
from library.create_tables import init_db
from library.services import (
    create_author, get_author_by_id, get_all_authors, update_author, delete_author,
    create_book, get_book_by_id, get_all_books, search_books_by_title, delete_book,
    create_student, get_student_by_id, get_all_students, update_student_grade,
    borrow_book, return_book, get_currently_borrowed_books
)

# DBni ishga tushirish
init_db()


#-----------------AUTHOR TEST-------------------#


# author = create_author(name='Xudoyberdi Tuhtaboyer', bio='Bolalar yozuvchisi')



# author_fetched = get_author_by_id(1)
# print("ID bo'yicha muallif:", author_fetched.name if author_fetched else None)

# updated_author = update_author(1, 'Alisher Navoiy', "Sheriyat mulkining sultoni")
# print("Yangilangan bio:", updated_author.bio if updated_author else None)




#-----------------BOOK TEST-------------------#



# book = create_book('Dunyoning Ishlari', author_id=1, published_year=2013, isbn='1234567890123')

# book_fetched = get_book_by_id(1)
# print("ID bo'yicha kitob:", book_fetched.title if book_fetched else None)

# results = search_books_by_title("Dunyoning")
# print("Qidiruv natijasi:", [b.title for b in results])



# #-----------------STUDENT TEST------------------#


# student = create_student("Ali Valiyev", "ali@mail.com", "10-A")


# student_fetched = get_student_by_id(1)
# print("ID bo'yicha talaba:", student_fetched.full_name if student_fetched else None)

# updated_student = update_student_grade(1, "11-B")
# print("Yangilangan sinf:", updated_student.grade if updated_student else None)




