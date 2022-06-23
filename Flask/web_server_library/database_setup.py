# для настройки баз данных

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy import Column, ForeignKey, Integer, Table

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

Base = declarative_base()

association_table = Table(

   "association",

   Base.metadata,

   Column("book_id", ForeignKey("books.id")),

   Column("author_id", ForeignKey("authors.id")),

)



class Book(Base):

   __tablename__ = 'books'

   id = Column(Integer, primary_key=True)

   title = Column(String(250), nullable=False)

   authors = relationship(

       "Author",

       secondary=association_table,

       back_populates='books')

   genre = Column(String(250))

   def __repr__(self):

       return f'{self.title}'



class Author(Base):

   __tablename__ = "authors"

   id = Column(Integer, primary_key=True)

   name = Column(String(250), nullable=False)

   books = relationship(

       'Book',

       secondary=association_table,

       back_populates='authors'

   )

   def __repr__(self):

       return f'{self.name}'



engine = create_engine('sqlite:///books-collections.db')

Base.metadata.create_all(engine)

