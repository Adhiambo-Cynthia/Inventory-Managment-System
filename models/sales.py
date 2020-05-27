from main import db
import datetime
class Sales(db.Model):
    __tablename__='new_sales'
    id = db.Column(db.Integer, primary_key=True)
    inv_id = db.Column(db.Integer,db.ForeignKey('new_inventories.id'))
    quantity = db.Column(db.Numeric,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
