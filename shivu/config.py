class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7086472788"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002197170236
    TOKEN = "7907388826:AAGZDMamWr4K0MSqR--2OKIB_pQ30Btm8tM"
    mongo_url = "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://wallpapers.com/images/hd/yor-forger-p5yg9x6z183pb9n9.jpg", "https://krita-artists.org/uploads/default/original/3X/2/f/2f50a5e8bd449d83961ded1ae154823c504a1c2b.jpeg"]
    SUPPORT_CHAT = "genanimeofcchat"
    UPDATE_CHAT = "genanimeofcchat"
    BOT_USERNAME = "GenWaifuGrabberBot"
    CHARA_CHANNEL_ID = "-1002197170236"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
