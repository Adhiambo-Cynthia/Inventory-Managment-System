from main import db
import datetime
class Stock(db.Model):
    __tablename__ = 'new_stock'
    id = db.Column(db.Integer, primary_key=True)
    inv_id = db.Column(db.Integer, db.ForeignKey('new_inventories.id'))
    stock = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
