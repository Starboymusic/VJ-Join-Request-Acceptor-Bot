from os import environ

API_ID = int(environ.get("API_ID", "19193584"))
API_HASH = environ.get("API_HASH", "6cce5fd44ffbeba47414ca91143dc8c2")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002493080239"))
ADMINS = int(environ.get("ADMINS", "6088500327"))
DB_URI = environ.get("DB_URI", "mongodb+srv://dbmongo568:@cluster0.kwl70.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")
