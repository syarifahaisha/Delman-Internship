from flask import Flask
import os
from os.path import join, dirname
from dotenv import load_dotenv
from database import db

from routes import route_bp



from flask_migrate import Migrate

app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# CONFIGURATION
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['AUTH_TOKEN_SECRET'] = os.getenv('AUTH_TOKEN_SECRET')

# DEFINE DB

# db.session.commit()
db.init_app(app)
with app.app_context():
    db.create_all()
    # migrate = Migrate(app, db)

# ROUTING
app.register_blueprint(route_bp)



if __name__ == '__main__':
    app.run()

# class Customer(db.Model):
#     __tablename__ = 'customer'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(12), unique=False, nullable=False)
#     address = db.Column(db.String(200), unique=False, nullable=False)
#     password = db.Column(db.String(50), unique=False, nullable=False)

#     def __init__(self, name, email, phone, address, password):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.address = address
#         self.password = password

# class Staff(db.Model):
#     __tablename__ = 'staff'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(12), unique=False, nullable=False)
#     address = db.Column(db.String(200), unique=False, nullable=False)
#     password = db.Column(db.String(50), unique=False, nullable=False)

#     def __init__(self, name, email, phone, address, password):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.address = address
#         self.password = password

# class Ebook(db.Model):
#     __tablename__ = 'ebook'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120), unique=False, nullable=False)
#     author = db.Column(db.String(120), unique=False, nullable=False)
#     synopsis = db.Column(db.String(250), unique=False, nullable=False)
#     price =  db.Column(db.Integer, unique=False, nullable=False)
#     image_url = db.Column(db.String(200), unique=False, nullable=False)
#     content_url = db.Column(db.String(200), unique=False, nullable=False)
#     children = relationship("Order")

#     def __init__(self, title, author, synopsis, price, image_url, content_url):
#         self.title = title
#         self.author = author
#         self.synopsis = synopsis
#         self.price = price
#         self.image_url = image_url
#         self.content_url = content_url

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_buku = db.Column(db.Integer, ForeignKey("ebook.id"), unique=False, nullable=False)
