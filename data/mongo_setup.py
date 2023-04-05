import mongoengine
from mongoengine import connect


def dbConectar(db_name: str):
    mongoengine.register_connection(alias='mdad', name=db_name)
    print("CONEXIÓN REALIZADA")
    return connect(db_name)


def dbDesconectar():
    mongoengine.disconnect(alias='mdad')
    print("Desconexión realizada")
