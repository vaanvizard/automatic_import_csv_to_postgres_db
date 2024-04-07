#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import os
import psycopg2

# Get user input
pw = input("Postgres Password: ")
db_name = input("New Database: ")


# Create New Database
conn = psycopg2.connect(host="localhost", dbname=f"postgres",
                        user="postgres", password=f"{pw}", port=5432)
cur = conn.cursor()
conn.autocommit = True

cur.execute(f"CREATE DATABASE {db_name};")

cur.close()
conn.close()


# Use sqlalchemy to connect to new db
url = URL.create(
    drivername='postgresql',
    username='postgres',
    password=pw,
    host='localhost',
    port=5432,
    database=db_name,
).render_as_string(hide_password=False)
db = create_engine(url)
new_db_conn = db.connect()


# Get csv file path and csv file names
path = "/home/lisa/SQL/" + input('CSV File Folder Name: ')
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
file_names = [name.split(".")[0] for name in files]

# Convert csv files to pd.DataFrame and import into postgres
for file in file_names:
    df = pd.read_csv(path + f"/{file}.csv")
    df.to_sql(file, con=new_db_conn, if_exists='replace', index=False)