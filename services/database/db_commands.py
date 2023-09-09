# from services.database.database import Database
#
#
# class UserCommand:
#
#     def __init__(self):
#         self.users_db = Database()
#
#     async def create_user_table(self):
#         self.users_db.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
#         id serial PRIMARY KEY,
#         user_id int,
#         user_name text,
#         first_name text,
#         full_name text);
#         """)
#         self.users_db.commit()
#
#     async def create_user(self):
#         self.users_db.execute("""
#         INSERT INTO TABLE users (
#                 user_id, user_name, first_name, full_name
#                 )
#             values (?, ?, ?, ?),
#             ('message.from_user.id',
#             'message.from_user.first_name',
#             'message.from_user.first_name',
#             'message.from_user.full_name'
#         """)
#         self.users_db.commit()
#
#     async def get_user(self):
#         self.users_db.execute()
#
#
