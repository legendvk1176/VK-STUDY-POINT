import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging = logging.getLogger("vk-study-point")
