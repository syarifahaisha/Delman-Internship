from sqlalchemy import ForeignKey

from database import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ebook = db.Column(db.Integer, ForeignKey("ebook.id"), unique=False, nullable=False)
    id_customer = db.Column(db.Integer, ForeignKey("customer.id"), unique=False, nullable=False)

    def __init__(self, id_ebook, id_customer):
        self.id_ebook = id_ebook
        self.id_customer = id_customer

    @property
    def serialize(self):
        return {
            'id': self.id,
            'id_ebook': self.id_ebook,
            'id_customer': self.id_customer,
        }