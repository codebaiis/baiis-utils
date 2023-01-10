import os
from typing import Dict, List

import psycopg2 as pg
from psycopg2.extensions import connection






def get_postgres_conn_from_env(db_code: str) -> connection:

    _validate_env_variables_for_pg_conn(db_code)

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


def _validate_env_variables_for_pg_conn(db_code: str) -> None:

    env_variables: Dict[str,str] = {
            f'{db_code}_DB': os.getenv(f'{db_code}_DB'),
            f'{db_code}_USER': os.getenv(f'{db_code}_USER'),
            f'{db_code}_PASSWORD': os.getenv(f'{db_code}_PASSWORD'),
            f'{db_code}_URL': os.getenv(f'{db_code}_URL')
        }

    missing_env_vars: List[str] = []

    for var_name, var_val in env_variables.items():
        if not var_val:
            missing_env_vars.append(var_name)

    if missing_env_vars:
        error_msg: str = f'  - the following environment variables need to be set:\n {missing_env_vars}'
        raise Exception(error_msg) 