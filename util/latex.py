import os
import subprocess

from settings import FileConf
from settings.config import TEX_SRC


def get_text_src():
    return open(FileConf.FileNames.tex_src, "r").read()


def itemize_list(items):
    content = {"items": r"\item " + r"\item ".join(items)}
    tex = r"""\begin{itemize}%(items)s\end{itemize}"""
    return tex % content


def create_table(head, rows):
    content = {"head": head + r" \\\hline", "rows": r"\\".join(rows)}
    tex = r"""\begin{table}[H]\centering\begin{tabular}{l|r} %(head)s %(rows)s \end{tabular}\end{table}"""
    return tex % content


def add_image(file_name, caption):
    content = {"filename": file_name, "caption": caption}
    tex = r"""\begin{figure}[H]\centering\includegraphics[width=0.8\textwidth]{%(filename)s}\caption{\label{} %(caption)s}\end{figure}"""
    return tex % content


class TexObj(object):

    def __init__(self, tex_string, path, file_name):
        self.tex_string = tex_string
        self.path = path
        self.file_name = file_name

    def compile(self, logger):
        generic_filename = os.path.join(self.path, self.file_name)
        pdf_name = generic_filename + ".pdf"
        tex_name = FileConf.FileNames.tex_src #generic_filename + ".tex"
        with open(tex_name, 'w') as f:
            f.write(self.tex_string)
        #cmd = ['pdflatex', '-interaction', 'nonstopmode', "-output-directory", self.path,  tex_name]
        cmd = ["rubber", "--into", self.path, "--pdf", tex_name]
        proc = subprocess.Popen(cmd)
        proc.communicate()
        for file_end in [".aux", ".log", ".toc", ".tex"]:
            temp = os.path.join(self.path, TEX_SRC.replace(".tex", "") + file_end)
            if os.path.exists(temp):
                os.unlink(temp)
            if os.path.exists(self.file_name + file_end):
                os.unlink(self.file_name + file_end)
        os.rename(
            src=os.path.join(FileConf.Paths.output, TEX_SRC.replace(".tex", ".pdf")),
            dst=pdf_name
        )
        logger.info("File {} generated.".format(pdf_name))

