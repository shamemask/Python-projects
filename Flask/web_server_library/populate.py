from sqlalchemy.orm import sessionmaker

# импортируем классы Book и Base из файла database_setup.py

from database_setup import Book, Base, Author

from app import engine

# Свяжим engine с метаданными класса Base,

# чтобы декларативы могли получить доступ через экземпляр DBSession

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# Экземпляр DBSession() отвечает за все обращения к базе данных

# и представляет «промежуточную зону» для всех объектов,

# загруженных в объект сессии базы данных.

session = DBSession()

# CREATE BOOK

# book1 = Book(title="Чистый Python1", genre="компьютерная литература1")

# book2 = Book(title="Чистый Python2", genre="компьютерная литература2")

# session.add_all(

#     [book1,book2]

# )

# author1 = Author(name='Оскар')

# author2 = Author(name='Оскар1')

# book1.authors.append(author1)

# book1.authors.append(author2)

# session.commit()

#

# f = session.query(Book).filter_by(title='Чистый Python1').all()

# print(f)

# CREATE Authors

author_1 = Author(name='Arthur', books=[Book(title="Грязный Python", genre="компьютерная литература")], )

session.add(author_1)

session.commit()

# session.add_all(

#     [author1,author2]

# )

