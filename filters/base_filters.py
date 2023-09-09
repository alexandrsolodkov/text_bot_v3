# from aiogram.filters import BaseFilter
# from aiogram.types import Message
#
#
# class NewUser(BaseFilter):
#     def __init__(self, users_list: list[int], message: Message) -> None:
#         self.users_list = users_list
#         self.user = message.from_user.id
#
#     async def __call__(self, message: Message) -> bool:
#         return self.user in self.users_list
