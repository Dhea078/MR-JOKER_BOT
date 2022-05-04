# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12790982  # integer value, dont use ""
    API_HASH = "b89c241fa8cf8a4ccf6b9145e9af22e4"
    BOT_ID = "5214056164"
    TOKEN = "5214056164:AAGDQlt_oz4qpMh2T5K08_ePlJBDrw-2Yzg"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1909694513  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Nero_KlaX"
    SUDO_USERS = "1909694513"
    SUPPORT_USERS = "1909694513"
    SUPPORT_CHAT = "ootdkece2"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001559785831
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001559785831
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://vfnbnuqvscphwm:e96ee1cb855c8fcb68e1009d4862d74cdd343637d9df401767e17fecd7b9069c@ec2-34-201-95-176.compute-1.amazonaws.com:5432/d8bg3ilqlsc3f2"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    HEROKU_API_KEY = "c02c6989-5e1a-4421-aff0-9cab27265c7e"
    HEROKU_APP_NAME = "steviaxrobot"
    BOT_USERNAME = "Spectras2bot"
    SPAMWATCH_API = "14b2g8c54l0L5QZvYa4zFuz022Xx6Sz6bqlOq2DzQ0ryBrnHbHMZppFFufkiTBMN"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ARQ_API_KEY = "FZPTXV-CEHJVF-OUDOLI-ZHHOIM-ARQ"
    ARQ_API_URL = "https://thearq.tech/"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    OPENWEATHERMAP_ID = ""
    VIRUS_API_KEY = ""
    REDIS_URL = ""
    LASTFM_API_KEY = ""
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    ALLOW_CHATS = ""
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1909694513" get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1909694513" get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1909694513" get_user_list("elevated_users.json", "tigers")
    WOLVES = "1909694513" get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "JQ6SZ9L9227B8BTZ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "TKDMWD1YZ2NQ"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "xyz"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = ""
    GENIUS_API_TOKEN = ""
    MONGO_DB = ""
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
