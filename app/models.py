from app import db
from sqlalchemy.sql import func
import json


class Fleet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    address = db.Column(db.String)

    def __repr__(self):
        return json.dumps({"fleet_id": self.id, "name": self.name, "address": self.address})


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    fleet_id = db.Column(db.Integer, db.ForeignKey('fleet.id'))

    def __repr__(self):
        return json.dumps({"user_id": self.id, "name": self.name, "surname": self.surname, 'fleet_id': self.fleet_id})


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_number = db.Column(db.String)
    brand = db.Column(db.String)
    fleet_id = db.Column(db.Integer, db.ForeignKey('fleet.id'))

    def __repr__(self):
        return json.dumps({"id": self.id, "brand": self.brand, "car_number": self.car_number, 'fleet_id': self.fleet_id})


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logger = db.Column(db.String)
    level = db.Column(db.String)
    trace = db.Column(db.String)
    message = db.Column(db.String)
    path = db.Column(db.String)
    method = db.Column(db.String)
    ip = db.Column(db.String)
    creation_date = db.Column(db.DateTime, nullable=False, server_default=func.now())

    __table_args__ = ({'sqlite_autoincrement': True},)
