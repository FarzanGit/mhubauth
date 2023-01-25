import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '6858661')) 
API_HASH = environ. get('API_HASH', '2a0a13be0ad40c86faabe3f5bf910c20') 
BOT_TOKEN = environ.get('BOT_TOKEN', "5902136501:AAEprrpiV6HsaLwMwWn4I2OBSioDK6RIKWw") 

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get("ADMINS", "").split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get("CHANNELS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get("AUTH_CHANNEL", '-1001624764526')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "-1001500903777").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Moviehub:Moviehub@cluster0.hopkcvg.mongodb.net/?retryWrites=true&w=majority") 
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0") 
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Tokyo Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", """**{file_name}**

__Size__ :**{file_size}**""")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
CUSTOM_FILE_CAPTION = None if FILE_CAPTION.strip() == "" else FILE_CAPTION
API_KEY = None if OMDB_API_KEY.strip() == "" else OMDB_API_KEY
