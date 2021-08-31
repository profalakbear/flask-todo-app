from flask_marshmallow import Marshmallow 

def create_marhsmellow_instance(app):
    ma = Marshmallow(app)
    return ma