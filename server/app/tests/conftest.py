import pytest
from app import app
from app.extensions import db


@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('app.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
