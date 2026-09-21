import os

# Legacy compatibility module. Runtime credentials must be configured in Heroku Config Vars.
api_id = int(os.environ.get("API_ID") or 0)
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")
LOG = int(os.environ.get("LOG", "0"))
