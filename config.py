class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
#connect to your postgresql,replace the password and dbname
class Development(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:cinadhis99@127.0.0.1:5432/sales_demo'
    SECRET_KEY='CynthiaAdhis'
class Production(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgres://prhysvlnbfrktf:d8b756cb01d30dbbb011bf8dd69c97a1fd92f0821646b7ce560e9dcaa9d1dca0@ec2-18-233-32-61.compute-1.amazonaws.com:5432/d8pv4s4i8mtljv'
    SECRET_KEY='CynthiaAdhis'




