from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import userRegister
from resources.item import Item,Items
from resources.store import Store,Stores
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='shubham'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)#calls identity function
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(Stores,'/stores')
api.add_resource(userRegister,'/register')
if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
