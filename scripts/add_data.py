import dask.dataframe as dd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def insert_data(db: str, table_name: str, file_path: str):
    db_url = f"mysql+pymysql://root:@localhost/{db}"
    engine = create_engine(db_url)
    if not database_exists(engine.url):
        create_database(engine.url)
    try:
        df = dd.read_csv(file_path, assume_missing = True)
    except:
        print(f'Error raised while trying to read {file_path}')
    df.to_sql(name=table_name, uri=db_url, if_exists='append', index=False)