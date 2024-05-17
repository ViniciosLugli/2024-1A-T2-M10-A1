from fastapi import APIRouter
from repositories.user import UserRepository
from pydantic import BaseModel
from prisma import Prisma

router = APIRouter()


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


@router.post("/users")
async def create_user(user: UserRegister):
    prisma = Prisma()
    await prisma.connect()
    try:
        user = await UserRepository(prisma).create_user(
            user.name, user.email, user.password
        )
    except Exception as e:
        return {"message": "Email already exists"}
    prisma.disconnect()

    return user


@router.get("/users")
async def read_users():
    prisma = Prisma()
    await prisma.connect()
    users = await UserRepository(prisma).get_users()
    prisma.disconnect()

    return users


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    prisma = Prisma()
    await prisma.connect()
    user = await UserRepository(prisma).delete_user(user_id)
    prisma.disconnect()

    return user
