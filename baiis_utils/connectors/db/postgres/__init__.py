import os
from typing import List

import psycopg2 as pg
from psycopg2.extensions import connection






def get_postgres_conn_from_env(db_code: str) -> connection:

    #TODO: validate env variables

    database: str = os.getenv(f'{db_code}_DB')
    user: str = os.getenv(f'{db_code}_USER')
    password: str = os.getenv(f'{db_code}_PASSWORD')
    host: str = os.getenv(f'{db_code}_URL')

    conn: connection = pg.connect(
        database=database,
        user=user,
        password=password,
        host=host
    )
    conn.autocommit = True

    return conn 