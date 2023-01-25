import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '19128968')) 
API_HASH = environ. get('API_HASH', '2f9e44d3ea2bc84ea1553ed6099fb2ae') 
BOT_TOKEN = environ.get('BOT_TOKEN', "985710912:AAFltFE7dOsnXkRgDNnyaJwcnvmoxVjeVvI") 

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get("ADMINS", "").split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get("CHANNELS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Tokyo:Tokyo@cluster0.ng8fsk2.mongodb.net/?retryWrites=true&w=majority") 
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0") 
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'movieshd_files')

# Messages
default_start_msg = """
**Hi, I'm Tokyo Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", """**{file_name}**(`{file_size}`) 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
കാണാൻ താല്പര്യമുള്ള മറ്റു സിനിമകൾ ഗ്രൂപ്പിൽ ചോദിക്കാം 
👇👇👇
💢GROUP      🔽
1) https://t.me/+WAASkCWDVwMHkY1s
2) https://t.me/+KOoNcfmnCvo4MmE1
3) https://t.me/+pYhVs_XYllVlNDI1""")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
CUSTOM_FILE_CAPTION = None if FILE_CAPTION.strip() == "" else FILE_CAPTION
API_KEY = None if OMDB_API_KEY.strip() == "" else OMDB_API_KEY
