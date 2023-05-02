from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from endpoints.depends import get_user_repository
from repositories.users import UserRepository
from models.user import User, UserIn

router = APIRouter()


@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
async def read_users(
        users_repository: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        offset: int = 0
):
    return await users_repository.get_all(limit, offset)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
        user: UserIn,
        users_repository: UserRepository = Depends(get_user_repository)
):
    return await users_repository.create(user)


@router.patch("/", response_model=User, status_code=status.HTTP_202_ACCEPTED)
async def update_user(
        user_id: int,
        user: UserIn,
        users_repository: UserRepository = Depends(get_user_repository)):
    return await users_repository.update(user_id, user)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, users_repository: UserRepository = Depends(get_user_repository)):
    return await users_repository.delete(user_id)


@router.get("/busy_users", status_code=status.HTTP_200_OK)
async def read_busy_users(
        users_repository: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        offset: int = 0):
    return await users_repository.get_busy_users(limit, offset)
