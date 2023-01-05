import os
import fnmatch


def get_files(root:str, regex:str, recursive:bool):
    """
    params:
        root(str): root dir path.
        regex(str): linux filename pattern - posix regular expression.
        recursive(bool): if true, search files recursively.
    returns:
        generator
    """
    if not os.path.exists(root):
        msg = f"{root} is not exists or not a directory."
        raise ValueError(msg)
    for par_dir, _, files in os.walk(root):
        if files:
            for file in fnmatch.filter(files, regex):
                yield os.path.join(par_dir, file)
        if not recursive:
            break
