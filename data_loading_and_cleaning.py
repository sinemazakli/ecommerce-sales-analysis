# %%
import pandas as pd
df=pd.read_excel("../data/orders.xlsx")

# %%
df.head()

# %%
df["InvoiceNo"].astype(str).str.startswith("C").value_counts()

# %%
df=df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# %%
df=df[df["Quantity"]>0]

# %%
df=df[df["UnitPrice"]>0]

# %%
df.info()

# %%
df["Total Price"]= df["Quantity"]*df["UnitPrice"]

# %%
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])

# %%
df["Month"]=df["InvoiceDate"].dt.month

# %%
df["Year"]=df["InvoiceDate"].dt.year

# %%
df[["InvoiceDate","Total Price","Month","Year"]].head()

# %%
df.to_csv("../data/clean_orders.csv", index=False)


# %%
import pandas as pd
from sqlalchemy import create_engine

# CSV dosyasını oku
df = pd.read_csv(r"C:\Temp\clean_orders.csv")

# SQL Server bağlantısı
engine = create_engine(
    "mssql+pyodbc://localhost/ECommerceAnalysis?driver=ODBC+Driver+18+for+SQL+Server?trusted_connection=yes"
)


# %%
import sqlalchemy
print(sqlalchemy.__version__)


# %%
import pandas as pd
from sqlalchemy import create_engine


# %%
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"..\data\clean_orders.csv", low_memory=False)


print(df.shape)
df.head()


# %%
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://localhost/ECommerceAnalysis"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

df.to_sql(
    name="orders",
    con=engine,
    if_exists="replace",  # tabloyu yeniden oluşturur
    index=False
)


# %%
import pyodbc
pyodbc.drivers()


# %%
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/ECommerceAnalysis"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
with engine.connect() as conn:
    print("Bağlantı başarılı 🎉")


# %%
import pandas as pd

df = pd.read_csv(
    r"..\data\clean_orders.csv",
    low_memory=False
)

df.head()


# %%
df.shape


# %%
df.to_sql(
    name="orders",
    con=engine,
    if_exists="replace",   # tablo varsa sil-yeniden yaz
    index=False
)


# %%



