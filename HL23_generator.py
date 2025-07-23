import oracledb as cx_Oracle
import os
from datetime import date
from database_credentials import username, password, dsn, interfaces_in
from dynamic_items_query import dynamic_items_query


def check_db_connection():
    try:
        with cx_Oracle.connect(user=username,password=password,dsn=dsn) as connection:
            print("Database connection successful, please wait for the results...")
            print('')
            return True
    except cx_Oracle.DatabaseError as e:
        print(f"Query >>check_db_connection<< connection failed: {e}. Please check your internet connection, if problem persists please visit Key Users.")
        return None
    

brand_matrix = {
    'UGG': 'UGG-C',
    'TEVA': 'HALL1B',
    'HOKA': 'HOKA-C',
    'SANUK': 'HALL1B',
    'KOOLABURRA': 'HALL1B',
    'DXLAB': 'HALL1B',
    'HOKA-A': 'HOKA-A',
    'HOKA-AA': 'HOKA-AA',
    'HOKA-B': 'HOKA-B',
    'HOKA': 'HOKA-C',
    'UGG-AA': 'UGG-AA',
    'UGG-A': 'UGG-A',
    'UGG-B': 'UGG-B',
    'UGG': 'UGG-C',
    'HOKA FOOTWEAR': 'HOKA-C',
    'KOOLABURRA FOOT': 'UGG-C',
    'TEVA FOOTWEAR': 'UGG-C',
    'UGG FOOTWEAR': 'UGG-C',
    'HOKA APPAREL': 'HOKA-C',
    'UGG POP': 'UGG-C',
    'UGG HOME': 'UGG-C',
    'HOKA ACCESSORIE': 'HOKA-C',
    'TEVA ACCESSORIE': 'UGG-C',
    'HOKA ACCESSORIE': 'HOKA-C',
    'UGG CARE': 'UGG-C',
    'HOKA PROMO': 'HOKA-C',
    'AHNU': 'UGG-C',
    'UGG ACCESSORIES': 'UGG-C',
    'HOKA POP': 'HOKA-C',
    'UGG POP': 'UGG-C',
    'TEVA POP': 'UGG-C',
    'TEVA APPAREL': 'UGG-C',
    'UGG APPAREL': 'UGG-C'
}


def get_dynamic_group():
    try:
        with cx_Oracle.connect(user=username, password=password, dsn=dsn) as connection:
            print("Querying for the list of items without dynamic groups")
            cursor = connection.cursor()
            cursor.execute(dynamic_items_query)
            results = cursor.fetchall()

        filename = 'HL23.'+ str(date.today()).replace('-','') + '00001.in'
        fullpath = os.path.join(interfaces_in, filename)

        with open(fullpath, 'w') as hl23:
            line_number = 0
            for result in results:

                line_number += 1

                line = f"{str(line_number).zfill(7)}HL23110001100{str(result[0]).zfill(13)}   30{brand_matrix[str(result[1])].ljust(10)}1\n"
                hl23.write(line)

    except cx_Oracle.DatabaseError as e:
        print(f"Error >>> {e} <<< when querying the list of items")
    

get_dynamic_group()