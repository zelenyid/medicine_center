import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_PASSWORD = os.environ['MONGODB_PASSWORD']
DATABASE_NAME = 'med'
DB_SOURCE = f'mongodb+srv://user:{DB_PASSWORD}@cluster.7pk1k.mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority'

JSON_KEYS_SERVICE_ACCOUNT = os.path.join(BASE_DIR, 'keys_service_account.json')
DISEASE_HISTORY_FILES_NAME = 'disease-history-files'
