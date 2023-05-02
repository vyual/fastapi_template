import sqlalchemy
from .base import metadata
import datetime

users_model = sqlalchemy.Table('users',
                               metadata,
                               sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True,
                                                 unique=True),
                               sqlalchemy.Column('name', sqlalchemy.String),
                               sqlalchemy.Column('job_title', sqlalchemy.String),
                               sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
                               sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow))
