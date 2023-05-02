from datetime import datetime
from typing import List, Optional

from loguru import logger

from db.tasks import tasks_model
from db.users import users_model
from models.user import User, UserIn
from repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, offset: int = 0) -> List:
        query = users_model.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query)

    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = users_model.select().where(users_model.c.id == user_id).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    # todo сделать один query
    async def get_busy_users(self, user_id: int, limit: int = 100, offset: int = 0) -> List:
        query = users_model.select()
        users = await self.database.fetch_all(query)
        logger.info(f"Found {len(users)} busy users. Here are: {users}")
        users_data = []
        for user in users:
            logger.debug(f"Found for user {user['id']}")
            query = tasks_model.select().where(tasks_model.c.assignee_id == user['id'])
            tasks = await self.database.fetch_all(query)
            logger.debug(f"Found {len(tasks)} tasks for user {user['id']}")
            user_data = {str(user['name']): {}}
            task_quantity = 0
            for task in tasks:
                if not task["completed"]:
                    user_data[user["name"]][task["id"]] = task["name"]
                    task_quantity += 1

            user_data[str(user["name"])]["task_quantity"] = task_quantity
            users_data.append(user_data)
        result = sorted(users_data, key=lambda x: list(x.values())[0]['task_quantity'], reverse=True)
        return result

    async def create(self, u: UserIn) -> User:
        user = User(name=u.name,
                    job_title=u.job_title,
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow())

        values = {**user.dict()}
        values.pop("id", None)

        query = users_model.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(id=id,
                    name=u.name,
                    job_title=u.job_title,
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow())

        values = {**user.dict()}
        values.pop("id", None)
        values.pop("created_at", None)

        query = users_model.update().where(users_model.c.id == id).values(**values)
        user.id = await self.database.execute(query)
        return user

    async def delete(self, id: int):
        query = users_model.delete().where(users_model.c.id == id)
        await self.database.execute(query)
