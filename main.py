import logging

from optparse import OptionParser

from settings import FileConf, LogConf
from util.latex import TexObj, get_text_src
from util.media import create_media


def create_tex(variables, file_name, path, logger):
    if not isinstance(variables, dict):
        raise ValueError("The parameter 'variables' must be an instance of dict.")
    logger.info("Function call: create_tex")
    tex_src = get_text_src()
    tex_formatted = tex_src % variables
    tex = TexObj(tex_string=tex_formatted, path=path, file_name=file_name)
    return tex


def main(filename, output_path, logger):
    variables = create_media()
    tex = create_tex(variables, filename, output_path, logger)
    logger.info("Method call: TexObj.compile()")
    tex.compile(logger)


if __name__ == "__main__":
    logger = LogConf.create(logging)
    parser = OptionParser()
    parser.add_option("--filename", type="string", help="Name of the output file.", default="report")
    parser.add_option("--output", type="string", help="Name of the output directory", default=FileConf.Paths.output)
    kwargs, _ = parser.parse_args(args=None, values=None)

    main(filename=getattr(kwargs, "filename"), output_path=getattr(kwargs, "output"), logger=logger)
