from app.extensions import db, bcrypt


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(hashed, password):
        return bcrypt.check_password_hash(hashed, password)

    def __repr__(self):
        return '<User %r>' % self.email
