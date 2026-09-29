import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Column, Integer, String, ARRAY
from sqlalchemy.orm import DeclarativeBase, sessionmaker
'''
# Загружаем переменные из файла .env
load_dotenv()

# Получаем параметры подключения
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Собираем URL подключения для PostgreSQL
DATABASE_URL = f"postresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
'''
class DatabaseManager:
    def __init__(self) -> None:
        # Загружаем переменные из файла .env
        load_dotenv()

        # Получаем параметры подключения
        self.__DB_USER = os.getenv("DB_USER")
        self.__DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.__DB_HOST = os.getenv("DB_HOST")
        self.__DB_PORT = os.getenv("DB_PORT")
        self.__DB_NAME = os.getenv("DB_NAME")

        # Собираем URL подключения для PostgreSQL
        self.__DATABASE_URL = (
            f"postgresql+psycopg2://{self.__DB_USER}:{self.__DB_PASSWORD}"
            f"@{self.__DB_HOST}:{self.__DB_PORT}/{self.__DB_NAME}"
        )

        # Создание движка
        self.engine = create_engine(self.__DATABASE_URL, echo=True)

        # Фабрика сессий
        self.__session_factory = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def create_tables(self) -> None:
        pass

class Base(DeclarativeBase): pass

class Experiments(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    architecture_type = Column(String)
    number_of_rows = Column(Integer)
    number_of_columns = Column(Integer)
    number_of_disconnected_input_streams = Column(ARRAY(Integer))
    number_of_application_completed = Column(Integer)
    number_of_application_dropped = Column(Integer)
    number_of_malfunctioning_neurons = Column(Integer)
    name_file_log = Column(String)



if __name__ == "__main__":
    test = DatabaseManager()