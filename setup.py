import logging
import os

from settings import FileConf, LogConf


def create_dir(dir_name, logger):
    if os.path.isdir(dir_name):
        logger.warning("Function create_dir: dir_name %s already exists.", dir_name)
        return dir_name
    os.makedirs(dir_name)
    logger.info("Function create_dir: dir_name %s created.", dir_name)
    return dir_name


def create_dirs(logger):
    create_dir(FileConf.Paths.resources, logger)
    create_dir(FileConf.Paths.data, logger)
    create_dir(FileConf.Paths.img, logger)
    create_dir(FileConf.Paths.output, logger)


if __name__ == "__main__":
    logger = LogConf.create(logging)
    create_dirs(logger)
