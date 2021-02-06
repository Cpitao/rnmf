import os
from interpreter import Interpreter
from name_generator import NameGenerator


if __name__ == "__main__":
    params = Interpreter.unpack_arguments()
    #for files_group in params["files"]:
    #    for file in files_group:
    #        new_name = NameGenerator.generate_name(params)
    #        os.rename(file, new_name)
    for old_name, name in NameGenerator.generate_name(params):
        if old_name is not None and name is not None:
            os.rename(old_name, name)
# rnmf [PATTERN] (--sort a/m) [FILES] 