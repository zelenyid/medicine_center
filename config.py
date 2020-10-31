import os

from pydantic import BaseModel

DB_PASSWORD = os.environ['MONGODB_PASSWORD']
DATABASE_NAME = 'med'
DB_SOURCE = f'mongodb+srv://user:{DB_PASSWORD}@cluster.7pk1k.mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority'

JWT_SECRET = 'MEDPROJ-SECRET'


class JwtSettings(BaseModel):
    authjwt_secret_key: str = JWT_SECRET
    authjwt_denylist_enabled: bool = True
    authjwt_header_type: str = 'Authorization-Token'

