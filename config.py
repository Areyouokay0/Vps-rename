import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5951942864:AAHj5HilQ7Ryu_ZOQYeUhZDtFEDfVYHSjQA")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "8206404"))
    API_HASH = os.environ.get("API_HASH", "e935d9b56e3fd2c05c743093efb761c9")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "858588280").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Aman:<password>@cluster0.zugrjwj.mongodb.net/?retryWrites=true&w=majority")
  
