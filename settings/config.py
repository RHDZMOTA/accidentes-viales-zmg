import json
import os

from os.path import join, dirname


configuration = json.loads(open(join(dirname(__file__), "conf.json"), "r").read())

# Read .env variables
RESOURCES_FOLDER = configuration.get("RESOURCES_FOLDER")
DATA_FOLDER = configuration.get("DATA_FOLDER")
IMG_FOLDER = configuration.get("IMG_FOLDER")
OUTPUT_FOLDER = configuration.get("OUTPUT_FOLDER")
LOG_FILE = configuration.get("LOG_FILE")
TEX_SRC = configuration.get("TEX_SRC")

# Project absolute path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Create complete paths
RESOURCES_PATH = join(PROJECT_DIR, RESOURCES_FOLDER)
OUTPUT_PATH = join(PROJECT_DIR, OUTPUT_FOLDER)


class FileConf:

    class Paths:
        output = OUTPUT_PATH
        resources = RESOURCES_PATH
        img = join(RESOURCES_FOLDER, IMG_FOLDER)
        data = join(RESOURCES_FOLDER, DATA_FOLDER)

    class FileNames:
        logger = join(PROJECT_DIR, LOG_FILE)
        tex_src = join(PROJECT_DIR, TEX_SRC)


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
