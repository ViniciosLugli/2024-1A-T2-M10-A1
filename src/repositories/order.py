import asyncio
from prisma import Prisma


class OrderRepository:
    def __init__(self, prisma: Prisma):
        self.prisma = prisma

    async def get_orders(self):
        return await self.prisma.order.find_many()

    async def create_order(
        self, name: str, description: str, price: float, quantity: int, user_cuid: str
    ):
        return await self.prisma.order.create(
            data={
                "name": name,
                "description": description,
                "price": price,
                "quantity": quantity,
                "userCuid": user_cuid,
            }
        )

    async def update_order(
        self,
        order_id: int,
        name: str,
        description: str,
        price: float,
        quantity: int,
        user_cuid: str,
    ):
        return await self.prisma.order.update(
            where={"id": order_id},
            data={
                "name": name,
                "description": description,
                "price": price,
                "quantity": quantity,
                "userCuid": user_cuid,
            },
        )

    async def delete_order(self, order_id: int):
        return await self.prisma.order.delete(where={"id": order_id})

    async def get_order_by_id(self, order_id: int):
        return await self.prisma.order.find_unique(where={"id": order_id})

    async def get_orders_by_user_id(self, user_cuid: str):
        return await self.prisma.order.find_many(where={"userCuid": user_cuid})
