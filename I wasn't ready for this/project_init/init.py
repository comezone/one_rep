from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import convertatation

DeclarativeBase = declarative_base()


class Post(DeclarativeBase): # table in database
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column('Имя', String)
    surname = Column('Фамилия', String)
    login = Column('логин', String)
    paswrd = Column('пароль', String)
    date = Column('Дата Рождения', TIMESTAMP)

    def __repr__(self):
        info: str = f'[Имя: {self.id}, Фамилия: {self.name},логин: {self.login},пароль: {self.paswrd}, Дата Рождения: {self.date}]'
        return info


class Crud: # Create ,read, update, delete
    engine = create_engine('postgresql+psycopg2://postgres:225690@localhost/Simalend')
    Session = sessionmaker(bind=engine)
    session = Session()

    @staticmethod
    def autorisation(login, password):
        engine = create_engine(f'postgresql+psycopg2://{login}:{password}@localhost/Simalend')
        try:
            engine.connect()
            return engine
        except:
            print(ValueError('Неверный логин или пароль!'))
            return False

    def create(self):
        print('Введите данные для регистрации: ')
        new_post = Post(name=input('Имя: ').strip(),
                        surname=input('Фамилия: ').strip(),
                        login=input('логин: ').strip(),
                        paswrd=input('пароль: ').strip(),
                        date=input('Дата Рождения: ').strip())
        self.session.add(new_post)
        self.session.commit()

    def read(self): # show a dict with columns from database
        x = self.session.query(Post.id,
                           Post.name,
                           Post.surname,
                           Post.login,
                           Post.paswrd,
                           Post.date).all()
        convert = convertatation.join(x)
        for i in convert:
            print(i)




    def update(self, tag, value, column):
        try:
            change = self.session.query(Post).get(tag)
            if column == 'имя':
                change.name = value
            elif column == 'фамилия':
                change.surname = value
            elif column == 'логин':
                change.login = value
            elif column == 'пароль':
                change.paswrd = value
            elif column == 'дата':
                change.date = value
            else:
                print('попробуйте выбрать из предложенных команд')
            self.session.commit()
        except:
            ValueError(print('id введен не верно, выберите номер'))

    def deleted(self, tag):
        self.session.query(Post).filter(Post.id == tag).delete()
        self.session.commit()


def main():
    print('Авторизируйтесь ')
    x = Crud().autorisation(input('логин: '), input('пароль: '))
    try:
        if not x:
            print('Попробуйте еще раз')
        else:
            print('Вы можете запись :', 'создать', 'изменить', 'удалить', 'посмотреть', sep='\n')
            answer = input().lower().strip()
            if answer == 'создать':
                Crud().create()
            elif answer == 'изменить':
                print("напишите что заменить: 'имя' 'фамилия' 'логин' 'пароль' 'дата'")
                Crud().update(tag=input('id: ').lower().strip(),
                              value=input('value: ').lower().strip(),
                              column=input('колонка: ').lower().strip())

            elif answer == 'посмотреть':
                Crud().read()

            elif answer == 'удалить':
                Crud().deleted(int(input('id: ')))
            else:
                print('Такой команды нет')


    except:
        print(ValueError('Неверное значение'))


if __name__ == "__main__":
    main()
