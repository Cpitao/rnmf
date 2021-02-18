import os
from interpreter import Interpreter
from name_generator import NameGenerator
from logger import Logger

if __name__ == "__main__":
    params = Interpreter.unpack_arguments()

    logger = Logger()
    
    for old_name, name, correct_name in NameGenerator.generate_name(params):
        if correct_name:
            os.rename(old_name, name)
        else:
            logger.omitted_files.append((old_name, name))


    if logger.omitted_files:
        logger.handle_omitted()
# rnmf [PATTERN] (--sort a/m) [FILES] 