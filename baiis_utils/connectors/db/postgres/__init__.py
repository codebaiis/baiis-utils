import os
from typing import Dict, List

import psycopg2 as pg
from psycopg2.extensions import connection






def get_postgres_conn_from_env(db_code: str) -> connection:

    database: str = os.getenv(f'{db_code}_DB')
    user: str = os.getenv(f'{db_code}_USER')
    password: str = os.getenv(f'{db_code}_PASSWORD')
    host: str = os.getenv(f'{db_code}_URL')

    env_variables: Dict[str,str] = {
            f'{db_code}_DB': database,
            f'{db_code}_USER': user,
            f'{db_code}_PASSWORD': password,
            f'{db_code}_URL': host
        }

    missing_env_vars: List[str] = []

    for var_name, var_val in env_variables.items():
        if not var_val:
            missing_env_vars.append(var_name)

    if missing_env_vars:
        error_msg: str = f'  - the following environment variables need to be set:\n {missing_env_vars}'
        raise Exception(error_msg) 

    conn: connection = pg.connect(
        database=database,
        user=user,
        password=password,
        host=host
    )
    conn.autocommit = True

    return conn 