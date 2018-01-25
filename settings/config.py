import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read .env variables
RESOURCES_FOLDER = os.environ.get("RESOURCES_FOLDER")
DATA_FOLDER = os.environ.get("DATA_FOLDER")
IMG_FOLDER = os.environ.get("IMG_FOLDER")
OUTPUT_FOLDER = os.environ.get("OUTPUT_FOLDER")
LOG_FILE = os.environ.get("LOG_FILE")
TEX_SRC = os.environ.get("TEX_SRC")

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
