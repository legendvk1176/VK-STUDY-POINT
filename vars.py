import os

API_ID = int(os.environ.get("API_ID") or 0)
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise RuntimeError(
        "Missing required environment variables: API_ID, API_HASH, BOT_TOKEN. "
        "Set them in Heroku Settings -> Config Vars."
    )
