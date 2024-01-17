import pandas as pd
from datetime import datetime


def write_to_file(kalorijas, tauki, oglhidrati, proteini):
    new_data = {
        'Datums': [datetime.now().strftime('%Y-%m-%d')],
        'Kalorijas_g': kalorijas,
        'Tauki_g': tauki,
        'Oglhidrati_g': oglhidrati,
        'Proteini_g': proteini
    }

    df_new = pd.DataFrame(new_data)
    excel_file_path = 'results.xlsx'

    try:
        existing_data = pd.read_excel(excel_file_path, engine='openpyxl')
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    if 'Datums' not in df_new.columns:
        df_new['Datums'] = df_new.index  
        
    if 'Datums' not in existing_data.columns:
        existing_data['Datums'] = existing_data.index  # Assuming 'Datums' should be the index

    date_exists = df_new['Datums'].isin(existing_data['Datums']).any() # pārbauda vai dati jau eksistē
    
    if date_exists:
        for col in ['Kalorijas_g', 'Tauki_g', 'Oglhidrati_g', 'Proteini_g']:
            existing_data[col] = existing_data[col].add(df_new[col].astype(existing_data[col].dtype), fill_value=0)
    else:
        existing_data = pd.concat([existing_data, df_new], ignore_index=True) # pievieno datus datu ierakstam

    existing_data.to_excel(excel_file_path, index=False, engine='openpyxl') # saglabā datu ierakstu exceli 

