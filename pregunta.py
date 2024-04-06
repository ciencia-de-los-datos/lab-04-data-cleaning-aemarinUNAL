"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv(
        "solicitudes_credito.csv", 
        sep=";",
        index_col=[0]   
    )

    df.dropna(how='any',inplace=True)

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('int')
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')

    for columna in df.columns:
        if df[columna].dtype == 'object':
            df[columna] = df[columna].str.lower()

    df['monto_del_credito'] = df['monto_del_credito'].str.replace(r'[$,]', '', regex=True).astype('float').astype('int')
    df['línea_credito'] = df['línea_credito'].str.replace(r'[_-]', ' ', regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.replace(r'[._-]', ' ', regex=True).replace(r'\s+', ' ', regex=True).str.rstrip()
    df['idea_negocio'] = df['idea_negocio'].str.replace(' de','').str.replace(' en','').str.replace(' y','').str.replace(' el','')
    df['barrio'] = df['barrio'].str.replace(r'[._-]', ' ', regex=True)
    df.drop_duplicates(inplace=True)
    
    return df
