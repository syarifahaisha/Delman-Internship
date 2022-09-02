from sqlalchemy.orm import relationship

from database import db

class Ebook(db.Model):
    __tablename__ = 'ebook'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    synopsis = db.Column(db.String(250), unique=False, nullable=False)
    price =  db.Column(db.Integer, unique=False, nullable=False)
    image_url = db.Column(db.String(200), unique=False, nullable=False)
    content_url = db.Column(db.String(200), unique=False, nullable=False)
    orders = relationship("Orders")

    def __init__(self, title, author, synopsis, price, image_url, content_url):
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.price = price
        self.image_url = image_url
        self.content_url = content_url

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'synopsis': self.synopsis,
            'price': self.price,
            'image_url': self.image_url,
            'content_url': self.content_url
        }