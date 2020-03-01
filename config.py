class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
#connect to your postgresql,replace the password and dbname
class Development(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:cinadhis99@127.0.0.1:5432/sales_demo'
    SECRET_KEY='CynthiaAdhis'
class Production(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:cinadhis99@127.0.0.1:5432/sales_demo'
    SECRET_KEY='CynthiaAdhis'




