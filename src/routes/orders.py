from fastapi import APIRouter
from repositories.order import OrderRepository
from pydantic import BaseModel
from prisma import Prisma

router = APIRouter()


class OrderCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    userCuid: str


@router.get("/orders/{order_id}")
async def read_order(order_id: int):
    prisma = Prisma()
    await prisma.connect()
    order = await OrderRepository(prisma).get_order_by_id(order_id)
    prisma.disconnect()

    return order if order else {"message": "Order not found"}


@router.get("/orders")
async def read_orders():
    prisma = Prisma()
    await prisma.connect()
    orders = await OrderRepository(prisma).get_orders()
    prisma.disconnect()

    return orders


@router.post("/orders")
async def create_order(order: OrderCreate):
    prisma = Prisma()
    await prisma.connect()
    order = await OrderRepository(prisma).create_order(
        order.name, order.description, order.price, order.quantity, order.userCuid
    )
    prisma.disconnect()
    return order


@router.put("/orders/{order_id}")
async def update_order(order_id: int, order: OrderCreate):
    prisma = Prisma()
    await prisma.connect()
    order = await OrderRepository(prisma).update_order(
        order_id,
        order.name,
        order.description,
        order.price,
        order.quantity,
        order.userCuid,
    )
    prisma.disconnect()

    return order if order else {"message": "Order not found"}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    prisma = Prisma()
    await prisma.connect()
    order = await OrderRepository(prisma).delete_order(order_id)
    prisma.disconnect()

    return {
        "message": "Order deleted successfully",
    }
