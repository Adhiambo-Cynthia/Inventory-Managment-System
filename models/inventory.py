from app import db
class Inventories(db.Model):
    __tablename__='new_inventories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,unique=True, nullable=False)
    type = db.Column(db.String(80))
    bp = db.Column(db.Numeric(80))
    sp = db.Column(db.Numeric(80))

    stock= db.relationship('Stock', backref='inventories', lazy=True)
    sales = db.relationship('Sales', backref='inventories', lazy=True)
