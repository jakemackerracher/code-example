from base import db
import uuid

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, default=uuid.uuid4())
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __repr__(self):
        return f"<User {self.name}>"