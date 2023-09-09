# import psycopg2
#
# from config_data import load_config
#
# config = load_config('.env')
#
#
# class Database:
#     def __init__(self):
#         self._conn = psycopg2.connect(
#             host=config.db.dh_host,
#             user=config.db.db_user,
#             password=config.db.db_password,
#             dbname=config.db.database
#         )
#         self._cursor = self._conn.cursor()
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self._conn.close()
#
#     @property
#     def connection(self):
#         return self._conn
#
#     @property
#     def cursor(self):
#         return self._cursor
#
#     def commit(self):
#         self.connection.commit()
#
#     def close(self, commit=True):
#         if commit:
#             self.commit()
#         self.connection.close()
#
#     def execute(self, sql, params=None):
#         self.cursor.execute(sql, params or ())
#
#     def fetchall(self):
#         return self.cursor.fetchall()
#
#     def fetchone(self):
#         return self.cursor.fetchone()
#
#     def query(self, sql, params=None):
#         self.cursor.execute(sql, params or ())
#         return self.fetchall()
