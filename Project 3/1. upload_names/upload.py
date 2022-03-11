import os

path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(f"path is {path}")

import pandas as pd

# Assign spreadsheet filename to `file`
file = path + '\названия точек.xlsm'
print(f"file is locate {file}")
# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Лист1')

print("sheet is sanding")
print(df1)

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/postgres")
with engine.begin() as connection:
    print(engine)
    df1.to_sql('endpoint_names',con=connection, if_exists="replace")
