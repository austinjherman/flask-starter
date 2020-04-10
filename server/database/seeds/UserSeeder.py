import uuid
from faker import Faker
from app.user.model import User
from app.extensions import db, bcrypt

fake = Faker()


def UserSeeder():

    user = User(
        uuid=uuid.uuid4(),
        name="Test",
        email="test@test.com",
        password=bcrypt.generate_password_hash('test').decode('utf-8')
    )
    db.session.add(user)

    for _ in range(9):
        user = User(
            uuid=uuid.uuid4(),
            name=fake.name(),
            email=fake.email(),
            password=bcrypt.generate_password_hash('test').decode('utf-8')
        )
        db.session.add(user)

    db.session.commit()
