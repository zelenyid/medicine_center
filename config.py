import os
from datetime import timedelta
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent

DB_PASSWORD = os.environ['MONGODB_PASSWORD']
DATABASE_NAME = 'med'
DB_SOURCE = f'mongodb+srv://user:{DB_PASSWORD}@cluster.7pk1k.mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority'
ADMIN_EXPIRES_DELTA = timedelta(minutes=5).seconds
ACCESS_EXPIRES_DELTA = timedelta(minutes=1).seconds
REFRESH_EXPIRES_DELTA = timedelta(minutes=5).seconds


JWT_SECRET = 'medsecret'


class JwtSettings(BaseModel):
    authjwt_secret_key: str = JWT_SECRET
    authjwt_denylist_enabled: bool = True
    authjwt_header_type: str = 'Authorization-Token'


JSON_KEYS_SERVICE_ACCOUNT = os.path.join(BASE_DIR, 'keys_service_account.json')
DISEASE_HISTORY_FILES_NAME = 'disease-history-files'
