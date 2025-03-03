from modules import create_app
from utils.config import config

# __init__ is the log module. Do not remove this.
# noinspection PyUnresolvedReferences
import __init__

spotipyn = create_app()

if __name__ == "__main__":
    spotipyn.run(threaded=True, host=config["host"], port=config["port"])
