from database import db
from BaseModel import BaseModel

class User(db.Model,BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(150),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)
    is_active = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def getData(self):
        return {
            'name': self.name,
            'email': self.email,
            'status': self.status,
        }
    
    @property
    def status(self):
        return "Active" if self.is_active else 'In Active'
    





