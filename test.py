from datetime import datetime
from library.create_tables import init_db
from library.services import (
    create_author, create_book,
    
)


init_db()
#-----------------AUTHOR-------------------#

# create_author(name='Xudoyberdi Tuhtaboyer', bio='Bolalar yozuvchisi')



#-----------------BOOK-------------------#
# create_book('Dunyoning Ishlari', 1, 2013, '1234567890123')