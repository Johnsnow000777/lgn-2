import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7057223899:AAFMF0DednEUdGnz0nK86gmYvLXdN4XUCV8")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29104992"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "284b770b42eb672c3a65ef656d0d65102")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ps705112:rahul@cluster0.td75ayj.mongodb.net/?retryWrites=true&w=majority")
