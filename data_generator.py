import duckdb

sf = 5
duckdb.sql('PRAGMA disable_progress_bar;SET preserve_insertion_order=false')
duckdb.sql(f"CALL dbgen(sf={sf});")


def generate_parquet_delta(table):
    duckdb.sql(f"select * from {table}").write_parquet(f'{table}.parquet')


def generate_data():
    for x in ['nation', 'region', 'customer', 'supplier', 'lineitem', 'orders', 'partsupp', 'part']:
        generate_parquet_delta(x)
