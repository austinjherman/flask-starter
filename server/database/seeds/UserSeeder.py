from faker import Faker
from app.user.model import User
from app.extensions import db, bcrypt


fake = Faker()


def UserSeeder():

    user = User(
        email="test@test.com",
        name="Test",
        password=bcrypt.generate_password_hash('test').decode('utf-8')
    )
    db.session.add(user)

    for _ in range(9):
        user = User(
            email=fake.email(),
            name=fake.name(),
            password=bcrypt.generate_password_hash('test').decode('utf-8')
        )
        db.session.add(user)

    db.session.commit()
