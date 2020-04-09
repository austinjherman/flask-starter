from app import app
from app.extensions import db
from flask.cli import FlaskGroup
from database.seeds.UserSeeder import UserSeeder


cli = FlaskGroup(app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('fake-users')
def seed_users():
    UserSeeder()


if __name__ == '__main__':
    cli()
