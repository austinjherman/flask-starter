from app import app
from app.extensions import db
from flask.cli import FlaskGroup


cli = FlaskGroup(app)


# new
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
