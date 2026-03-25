from database import db

class BaseModel:

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self,data):
        for key,value in data.items():
            setattr(self,key,value)
        db.session.commit()

    def create(self,data):
        for key,value in data.items():
            setattr(self,key,value)
        db.session.add(self)
        db.session.commit()


    
