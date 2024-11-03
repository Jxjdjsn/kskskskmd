# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = getenv("BOT_TOKEN", "6795643222:AAEjx5lFtIUIU1TFilv1hhF-c9xcki1oDPk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6692315925").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority
")
LOG_GROUP = getenv("LOG_GROUP", "-1002280792119")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002242042999"))
