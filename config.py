import os
import codecs

DB_PASSWORD = os.environ['MONGODB_PASSWORD']
DATABASE_NAME = 'med'
DB_SOURCE = f'mongodb+srv://user:{DB_PASSWORD}@cluster.7pk1k.mongodb.net/{DATABASE_NAME}?retryWrites=true&w=majority'
# JSON_KEYS_SERVICE_ACCOUNT = '{}\\{}'.format(os.getcwd(), 'keys_service_account.json')
