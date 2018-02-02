import json
import os

from os.path import join, dirname


config_app = json.loads(open(join(dirname(__file__), "config.json"), "r").read())

# Read .env variables
RESOURCES_FOLDER = config_app["folders"].get("RESOURCES_FOLDER")
DATA_FOLDER = config_app["folders"].get("DATA_FOLDER")
IMG_FOLDER = config_app["folders"].get("IMG_FOLDER")
OUTPUT_FOLDER = config_app["folders"].get("OUTPUT_FOLDER")
LOG_FILE = config_app["files"].get("LOG_FILE")
TEX_SRC = config_app["files"].get("TEX_SRC")

# Project absolute path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Create complete paths
RESOURCES_PATH = join(PROJECT_DIR, RESOURCES_FOLDER)
OUTPUT_PATH = join(PROJECT_DIR, OUTPUT_FOLDER)
DATA_PATH = join(RESOURCES_PATH, DATA_FOLDER)


class FileConf:

    class Paths:
        output = OUTPUT_PATH
        resources = RESOURCES_PATH
        data = DATA_PATH
        img = join(RESOURCES_FOLDER, IMG_FOLDER)

    class FileNames:
        logger = join(PROJECT_DIR, LOG_FILE)
        tex_src = join(PROJECT_DIR, TEX_SRC)
        accidents_per_indicator = join(DATA_PATH, config_app["files"].get("accidents_per_indicator"))
        accidents_per_year = join(DATA_PATH, config_app["files"].get("accidents_per_year"))
        death_by_alcohol = join(DATA_PATH, config_app["files"].get("death_by_alcohol"))
        death_zmg = join(DATA_PATH, config_app["files"].get("death_zmg"))


class LogConf:
    path = FileConf.FileNames.logger
    format = '%(asctime)s %(levelname)s:%(message)s'
    datefmt = '%m/%d/%Y %I:%M:%S %p'

    @staticmethod
    def create(logging):
        logging.basicConfig(format=LogConf.format, filename=LogConf.path, datefmt=LogConf.datefmt, level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.StreamHandler())
        return logger
