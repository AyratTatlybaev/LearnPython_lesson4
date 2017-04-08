from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Выбираем с какой БД будем работать: blog.sqlite - файл с базой 
engine = create_engine('sqlite:///blog.sqlite')
#сессия - соеднинение с БД
db_session = scoped_session(sessionmaker(bind=engine))
#создаём класс для БД - декларативный
Base = declarative_base()
#создаём возможность делать запросы
Base.query = db_session.query_property()

#Наш class User наследуется от Base
class User(Base):
	#атрибут класса 
    __tablename__ = 'users'
    #атрибут класса колонки 
    id = Column(Integer, primary_key=True)
    #string - длина строки
    first_name = Column(String(50))
    #string - длина строки
    last_name = Column(String(50))
    #string - длина строки, 
    #unique - БД будет сама делать проверку на уникальность email 
    email = Column(String(120), unique=True)
    #Связь между таблицами, backref - то как связь будет выглядеть со стороны
    posts = relationship('Post', backref='author')

    #метод класса
    #__init__ конструктор класса
    def __init__(self, first_name=None, last_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    #метод класса
    #вывод first_name и last_name
    def __repr__(self):
        return '<User {} {} {}>'.format(self.first_name, self.last_name, self.email)

class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	title = Column(String(140))
	#ссылка на картинку
	image = Column(String(500))
	published = Column(DateTime)
	content = Column(Text)
	user_id = Column(Integer, ForeignKey('users.id'))
	

	def __init__(self, title=None, image=None, published=None, content=None, user_id=None):
		self.title = title
		self.image = image
		self.published = published
		self.content = content
		self.user_id = user_id

	def __repr__(self):
		return '<Post {}>'.format(self.title)

#Создадим нашу базу данных
if __name__ == "__main__":
	Base.metadata.create_all(bind=engine)