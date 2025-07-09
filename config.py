import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27332436"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e4e48674defb04a12d480bed130c5243")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7239855276"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://admin:aditya1234@aditya.ucgmk91.mongodb.net/?retryWrites=true&w=majority&appName=aditya") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
