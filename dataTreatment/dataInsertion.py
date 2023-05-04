from data.Gasolinera import Gasolinera


def insertData(df):
    for index, row in df.iterrows():

        # create a Point object with longitude, latitude coordinates
        point = {
            'type': 'Point',
            'coordinates': [row['Longitud'], row['Latitud']]
        }

        g = Gasolinera(
            rid=row['Id'],
            cp=row['Codigo_postal'],
            direccion=row['Direccion'],
            provinvia=row['Provincia'],
            municipio=row['Municipio'],
            localidad=row['Localidad'],
            margen=row['Margen'],
            loc=point,
            precio_g1=row['Precio_g1'],
            precio_g2=row['Precio_g2'],
            precio_g3=row['Precio_g3'],
            precio_g4=row['Precio_g4'],
            precio_g5=row['Precio_g5'],
            precio_g6=row['Precio_g6'],
            precio_g7=row['Precio_g7'],
            precio_g8=row['Precio_g8'],
            precio_g9=row['Precio_g9'],
            rotulo=row['Rotulo'],
            tipo=row['Tipo_venta'],
            rem=row['Rem'],
            horario=row['Horario'],
            fecha=row['Fecha']
        )

        g.save()
