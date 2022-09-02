from lib2to3.pgen2 import token
from flask import request, jsonify, make_response
from models.Ebook import Ebook
from auth_middleware import token_required_admin
from database import db


@token_required_admin
def getAllEbook(current_user):
    if request.method == 'GET':
        ebook = Ebook.query.all()
        result = jsonify(data=[i.serialize for i in ebook])
        return result

def getAllEbook2():
    if request.method == 'GET':
        ebook = Ebook.query.all()
        result = jsonify(data=[i.serialize for i in ebook])
        return result

@token_required_admin
def addEbook(current_user):
    if request.method == 'POST':
        req_body = request.get_json()
        title = req_body.get('title', None)
        author = req_body.get('author', None)
        synopsis = req_body.get('synopsis', None)
        price =  req_body.get('price', None)
        image_url = req_body.get('image_url', None)
        content_url = req_body.get('content_url', None)

        if (None not in (title, author, author, synopsis, price, image_url, content_url)):
            if (db.session.query(Ebook).filter(Ebook.title == title, Ebook.author == author).count() == 0):
                try: 
                    data = Ebook(title=title, author=author, synopsis=synopsis, price=price, image_url=image_url, content_url=content_url)
                    db.session.add(data)
                    db.session.commit()
                    return make_response({'message': 'Ebook sucessfully added' }, 200)
                except:
                    return make_response({'message': 'Error server' }, 500)
            else:
                return make_response({'message' : 'Error. Book already registered'}, 400)
        else:
            return make_response('every field must be filled', 400)

@token_required_admin
def getEbookByID(current_user, id):
    if request.method == 'GET':
        ebook = Ebook.query.filter_by(id=id).first()
        if (ebook):
            data = {    
                "title" : ebook.title,
                "author" : ebook.author,
                "synopsis" : ebook.synopsis,
                "price" : ebook.price,
                "image_url" : ebook.image_url,
                "content_url" : ebook.content_url
            }

            return jsonify(data)
        else:
            return make_response({'message': 'Ebook not found' }, 400)

def getEbookByID2(id):
    if request.method == 'GET':
        ebook = Ebook.query.filter_by(id=id).first()
        if (ebook):
            data = {    
                "title" : ebook.title,
                "author" : ebook.author,
                "synopsis" : ebook.synopsis,
                "price" : ebook.price,
                "image_url" : ebook.image_url,
                "content_url" : ebook.content_url
            }

            return jsonify(data)
        else:
            return make_response({'message': 'Ebook not found' }, 400)

@token_required_admin
def editEbookByID(current_user, id):
    if request.method == 'PUT':
        print(id)
        try:
            req_body = request.get_json()
            title = req_body.get('title', None)
            author = req_body.get('author', None)
            synopsis = req_body.get('synopsis', None)
            price =  req_body.get('price', None)
            image_url = req_body.get('image_url', None)
            content_url = req_body.get('content_url', None)

            ebook = Ebook.query.filter_by(id=id).update(dict(
                title=title, 
                author = author,
                synopsis = synopsis,
                price = price,
                image_url = image_url,
                content_url = content_url))


            db.session.commit()

            return make_response({'message': 'Ebook information successfully updated' }, 200)
        except:
            return make_response({'message': 'Something else went wrong' }, 500)


@token_required_admin
def deleteEbookByID(current_user, id):
    if request.method == 'DELETE':
        try:
            ebook = Ebook.query.filter_by(id=id).delete()
            db.session.commit()

            return make_response({'message': 'Ebook information successfully deleted' }, 200)
        except:
            return make_response({'message': 'Something else went wrong' }, 500)