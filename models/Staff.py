from database import db

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=False, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)

    def __init__(self, name, email, phone, address, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'password': self.password
        }