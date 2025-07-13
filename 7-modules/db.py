import psycopg2
from psycopg2 import sql

# Connection details
HOST = "hh-pgsql-public.ebi.ac.uk"
PORT = 5432
DBNAME = "pfmegrnargs"
USER = "reader"
PASSWORD = "NWDMCE5xdipIjRrp"

def connect_db():
    try:
        conn = psycopg2.connect(
            host=HOST,
            port=PORT,
            dbname=DBNAME,
            user=USER,
            password=PASSWORD
        )
        print("✅ Connection successful!")
        return conn
    except Exception as e:
        print("❌ Connection failed:", e)
        return None

def list_databases(conn):
    print("\n--- Databases ---")
    try:
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        dbs = cur.fetchall()
        for db in dbs:
            print(db[0])
        cur.close()
    except Exception as e:
        print("Error listing databases:", e)

def list_tables(conn):
    print("\n--- Tables in current database ---")
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT table_schema, table_name
            FROM information_schema.tables
            WHERE table_type = 'BASE TABLE'
            AND table_schema NOT IN ('pg_catalog', 'information_schema');
        """)
        tables = cur.fetchall()
        for schema, table in tables:
            print(f"{schema}.{table}")
        cur.close()
    except Exception as e:
        print("Error listing tables:", e)

def main():
    conn = connect_db()
    if conn:
        list_databases(conn)
        list_tables(conn)
        conn.close()

if __name__ == "__main__":
    main()
