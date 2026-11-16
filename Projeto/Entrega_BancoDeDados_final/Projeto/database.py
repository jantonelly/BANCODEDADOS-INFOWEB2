"""Conexão SQL Server configurada por variáveis de ambiente (.env)."""
import os
import pyodbc
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()


@contextmanager
def connect():
    driver = os.getenv("SQLSERVER_DRIVER", "ODBC Driver 18 for SQL Server")
    server = os.getenv("SQLSERVER_SERVER", r"localhost\SQLEXPRESS")
    database = os.getenv("SQLSERVER_DATABASE", "AgendaServicos")
    username = os.getenv("SQLSERVER_USERNAME", "")
    password = os.getenv("SQLSERVER_PASSWORD", "")
    encrypt = os.getenv("SQLSERVER_ENCRYPT", "no")
    trust = os.getenv("SQLSERVER_TRUST_CERTIFICATE", "yes")
    auth = f"UID={username};PWD={password};" if username else "Trusted_Connection=yes;"
    connection_string = (
        f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};{auth}"
        f"Encrypt={encrypt};TrustServerCertificate={trust};"
    )
    cn = pyodbc.connect(connection_string)
    try:
        yield cn
        cn.commit()
    except Exception:
        cn.rollback()
        raise
    finally:
        cn.close()
