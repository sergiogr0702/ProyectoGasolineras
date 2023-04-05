from app.Application import App
from data.Gasolinera import Gasolinera
from dataTreatment.dataCleanup import cleanCSV
from data.mongo_setup import dbConectar, dbDesconectar
import sys

from dataTreatment.dataInsertion import insertData

if __name__ == '__main__':

    if sys.argv.__len__() != 2:
        print("Error:El programa se necesita ejecutar de la siguiente manera: python main.py <filename_with_csv>")
        sys.exit(1)

    # Lectura y rpeparacion de los datos leidos desde el csv
    print("---Preparando datos para la insercion---")
    df = cleanCSV(sys.argv[1])

    #Conexion con las base de datos
    db = dbConectar('MDAD')

    #Creacion de los indices sobre la coleccion gasolineras antes de insertar los datos
    Gasolinera.ensure_indexes()

    # Get the indexes for the collection
    gasolinera_collection = Gasolinera._get_collection()
    indexes = gasolinera_collection.index_information()

    # Print the indexes
    print("Los indices creados son:")
    print(indexes)

    # Insercion de los datos leidos desde el csv en la base de datos
    print("---Insertando datos en MongoDB---")
    insertData(df)
    print("---Datos insertados---")

    app = App()
    app.mainloop()

    # Borrado de la base de datos para que se quede en el mismo estado que al principio
    db.drop_database('MDAD')
    print("---Base de datos eliminada---")

    # Desconexion con las base de datos
    dbDesconectar()
