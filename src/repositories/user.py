import asyncio
from prisma import Prisma


class UserRepository:
    def __init__(self, prisma: Prisma):
        self.prisma = prisma

    async def get_user_by_email(self, email: str):
        return await self.prisma.user.find_first(where={"email": email})

    async def create_user(self, name: str, email: str, password: str):
        return await self.prisma.user.create(
            data={"name": name, "email": email, "password": password}
        )

    async def get_user_by_id(self, user_id: str):
        return await self.prisma.user.find_first(where={"cuid": user_id})

    async def get_users(self):
        return await self.prisma.user.find_many()

    async def delete_user(self, user_id: str):
        return await self.prisma.user.delete(where={"cuid": user_id})
