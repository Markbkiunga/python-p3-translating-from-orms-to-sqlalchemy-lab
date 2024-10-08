from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_table(base, engine):
    pass
    Session = sessionmaker(bind=engine)
    session = Session()
    base.metadata.create_all(engine)
    return session


def save(session, dog):
    pass
    session.add(dog)
    session.commit()


def get_all(session):
    pass
    return session.query(Dog).all()


def find_by_name(session, name):
    pass
    return session.query(Dog).filter(Dog.name == name).first()


def find_by_id(session, id):
    pass
    return session.query(Dog).filter(Dog.id == id).first()


def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()


def update_breed(session, dog, breed):
    pass
    dog.breed = breed
    session.commit()
