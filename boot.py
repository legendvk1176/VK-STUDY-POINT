import os
import runpy
import sys
import traceback


def fail(message):
    print(f"[BOOT ERROR] {message}", flush=True)
    raise SystemExit(1)


required = ("API_ID", "API_HASH", "BOT_TOKEN")
missing = [name for name in required if not os.environ.get(name)]
if missing:
    fail("Missing Heroku Config Vars: " + ", ".join(missing))

try:
    int(os.environ["API_ID"])
except ValueError:
    fail("API_ID must contain only the numeric Telegram API ID")

print("[BOOT] Environment validated; starting main.py", flush=True)
try:
    runpy.run_path("main.py", run_name="__main__")
except SystemExit:
    raise
except Exception:
    print("[BOOT ERROR] main.py crashed:", flush=True)
    traceback.print_exc()
    sys.exit(1)
