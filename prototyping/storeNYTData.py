import pandas as pd
from sqlalchemy import create_engine

# exec(open("storeNYTData.py").read())

df = pd.read_csv("NYT_Data.csv")
engine = create_engine(
    "[DATABASE ENGINE]", echo=True)
sql_connection = engine.connect()
sql_table = "articles"
df.to_sql(sql_table, sql_connection, if_exists="replace",
          index=False, chunksize=100)
sql_connection.close()
