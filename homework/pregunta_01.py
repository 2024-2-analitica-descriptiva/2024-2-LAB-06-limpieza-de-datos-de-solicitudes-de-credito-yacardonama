"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    #sexo = 2 
    #tipo de emprendimiento = 4 
    #idea de negocio = 75 
    #barrio = 225
    #estrato= 4
    #comuna = 21
    #fecha = 795
    #monto = 277
    #linea crédito = 9

    ruta= "./files/input/solicitudes_de_credito.csv"
    df = pd.read_csv(ruta, sep=';')

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df['sexo'] = df['sexo'].str.lower()

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()

    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].replace('-', ' ', regex=True)
    df['idea_negocio'] = df['idea_negocio'].replace('_', ' ', regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.strip()

    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace(r'\.', ' ', regex=True)
    df['barrio'] = df['barrio'].replace('_', ' ', regex=True)
    df['barrio'] = df['barrio'].replace('-', ' ', regex=True)

    df['estrato'] = df['estrato'].astype(str)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(str)

    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '').str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].astype(float).astype(int)

    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.strip()
    df['línea_credito'] = df['línea_credito'].str.replace(r'\.', ' ', regex=True)
    df['línea_credito'] = df['línea_credito'].replace('-', ' ', regex=True)
    df['línea_credito'] = df['línea_credito'].replace('_', ' ', regex=True)
    df['línea_credito'] = df['línea_credito'].replace('  ', ' ', regex=True)

    # Función para convertir a formato dd/mm/yyyy
    def convertir_fecha(fecha):
        for fmt in ['%d/%m/%Y', '%Y/%m/%d', '%d-%m-%Y', '%Y%m%d']:
            try:
                return pd.to_datetime(fecha, format=fmt).strftime('%d/%m/%Y')
            except ValueError:
                pass
        return None  # Si no coincide con ningún formato

    # Aplicar la función a la columna 'fecha'
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(convertir_fecha)

    df = df.drop(['Unnamed: 0'], axis=1)
    df.drop_duplicates(inplace=True)

    ruta_archivo = "./files/output/solicitudes_de_credito.csv"

    directorio = os.path.dirname(ruta_archivo)
    if directorio: 
        os.makedirs(directorio, exist_ok=True)

    df.to_csv(ruta_archivo, sep=";", index=False, encoding='utf-8')

pregunta_01()