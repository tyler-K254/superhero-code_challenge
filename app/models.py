from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)

class Power(db.Model):
    __tablename__ = 'Power'



class HeroPower(db.Model):
    __tablename__ = 'HeroPower'

    power_id = db.Column(db,Integer, db.ForeignKey('power.id'))
    hero_id  = db.Column(db.Integeer, db.Foregin('hero.id'))



    
# add any models you may need. 