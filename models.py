from db import db

class usuario(db.model):
    __tablename__ = 'usuario'
    id = db.column(db.interger,primary_key= True)
    nome = db.column(db.string(30), unique=True)
    senha = db.column(db.string())