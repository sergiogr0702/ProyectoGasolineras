import pandas as pd
import os


def cleanCSV(filePath):
    # read the CSV file
    df = pd.read_csv(filePath)

    # remove inncesary columns
    df = df.drop(columns=['X', 'Y', 'Field1', 'Toma_de_da', 'Tipo_servi', 'Precio_g_1', 'Precio_g_4', 'Precio_g_8',
                          'Precio_bio', 'F__bioalco', 'Precio_b_1', 'F__éster_', 'Precio_hid'])

    # rename the columns
    df = df.rename(columns={'FID': 'Id', 'Código_po': 'Codigo_postal', 'Dirección': 'Direccion',
                            'Precio_gas': 'Precio_g1', 'Precio_g_2': 'Precio_g2', 'Precio_g_3': 'Precio_g3',
                            'Precio_g_5': 'Precio_g4', 'Precio_g_6': 'Precio_g5',
                            'Precio_g_7': 'Precio_g6', 'Precio_g_9': 'Precio_g7',
                            'Precio__10': 'Precio_g8', 'Precio__11': 'Precio_g9',
                            'Rótulo': 'Rotulo', 'Rem_': 'Rem', 'fecha': 'Fecha'})

    directory = os.path.dirname(filePath)

    # export to csv with accents
    df.to_csv(directory + '\\Nuevo.csv', index=False, encoding='utf-8-sig')

    return df
