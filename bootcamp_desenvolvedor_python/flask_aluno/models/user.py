from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))
    cpf = db.Column(db.String(11), nullable=False)

    def serialize(self):
        return{'id': self.id,
               'name': self.name,
               'phone': self.phone,
               'address': self.address,
               'cpf': self.cpf}