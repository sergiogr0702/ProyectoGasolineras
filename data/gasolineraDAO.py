from data.Gasolinera import Gasolinera


class GasolineraDAO:

    def db_consultar_gasolineras_por_ubicacion(self, latitude, longitude, distance):

        gasolineras = Gasolinera\
            .objects(loc__geo_within_sphere=[(latitude, longitude), distance / 6378.1])\
            .order_by('-precio_g1')

        return sorted(gasolineras, key=lambda g: 0 if g.precio_g1 == 0 else 1)

