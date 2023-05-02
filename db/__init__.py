from .users import users_model
from .tasks import tasks_model
from .base import metadata, engine

metadata.create_all(engine)
