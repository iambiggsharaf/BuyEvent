from peewee import *
import datetime
db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db
    
class Product(BaseModel):
    id = IntegerField(primary_key = True)
    name = CharField()
    cost = IntegerField()
    
class Client(BaseModel):
    id = IntegerField(primary_key = True)
    phone = CharField()
    email = CharField()
    
class Event(BaseModel):
    id = IntegerField(primary_key = True)
    product = ForeignKeyField(Product)
    client = ForeignKeyField(Client)
