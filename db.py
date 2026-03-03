from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    max_rps = db.Column(db.Integer, default=100)
    sensitivity = db.Column(db.String(10), default="medium")
    auto_block = db.Column(db.Boolean, default=False)

class Blacklist(db.Model):
    ip = db.Column(db.String(50), primary_key=True)
    reason = db.Column(db.String(200))
    added_at = db.Column(db.String(50), default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class Whitelist(db.Model):
    ip = db.Column(db.String(50), primary_key=True)
    purpose = db.Column(db.String(200))
    added_at = db.Column(db.String(50), default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
