import datetime
import mongoengine as mongoengine


class Gasolinera(mongoengine.Document):
    rid = mongoengine.LongField(required=True, unique=True)
    provinvia = mongoengine.StringField(required=True)
    municipio = mongoengine.StringField(required=True)
    cp = mongoengine.IntField()
    direccion = mongoengine.StringField(text=True)
    margen = mongoengine.StringField()
    loc = mongoengine.PointField(geospatial_index=True)
    precio_g1 = mongoengine.FloatField(default=0.0)
    precio_g2 = mongoengine.FloatField(default=0.0)
    precio_g3 = mongoengine.FloatField(default=0.0)
    precio_g4 = mongoengine.FloatField(default=0.0)
    precio_g5 = mongoengine.FloatField(default=0.0)
    precio_g6 = mongoengine.FloatField(default=0.0)
    precio_g7 = mongoengine.FloatField(default=0.0)
    precio_g8 = mongoengine.FloatField(default=0.0)
    precio_g9 = mongoengine.FloatField(default=0.0)
    rotulo = mongoengine.StringField(text=True)
    tipo = mongoengine.StringField()
    rem = mongoengine.StringField()
    horario = mongoengine.StringField()
    fecha = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'mdad',
        'collection': 'gasolineras',
        'indexes': [
            {'fields': [('rotulo', 'text'), ('direccion', 'text')], 'weights': {'rotulo': 10, 'direccion': 5},
             'default_language': 'spanish'},
            {'fields': ['municipio', 'rem']},
            {'fields': ['loc']}
        ]
    }
