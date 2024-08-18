import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24594907"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cebf6f41df2f1cfe56e25beac945ac36")

#Database 
DB_URI = os.environ.get("DB_URI", "http://92@cluster0.n0zhthj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
