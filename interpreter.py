import sys
import os
from name_generator import NameGenerator

class Interpreter:
    class ArgumentError(Exception):
        pass

    def validate_arguments(params):
        sorting_methods = ['a', 'm', None]
        # a for alphabetical sorting
        # m for sorting by last modification date (the oldest go first)
        # None for no sorting (input order)

        if params["sort"] not in sorting_methods:
            print("rnmf: invalid argument {} for --sort".format(params["sort"]))
            exit(-1)

        NameGenerator.validate_pattern(params["pattern"])

        if not params["files"]:
            print("rnmf: no files specified")
            exit(-1)

        for group in params["files"]:
            for file in group:
                if not os.path.exists(file):
                    print("rnmf: file \"{}\" does not exist".format(file))
                    exit(-1)


    def unpack_arguments():
        # patterns
        # with \i denoting where to put the index(at the end by default)
        # if files are grouped, then \g denotes group index
        
        sort_aliases = ('--sort', '-s')
        # sort alphabetically / by modification date
        # to sort numerically it is advised to input already sorted file names

        params = {
            "sort": None,
            "pattern": None,
            "files": [],
            "overwrite": False
        }
        args = sys.argv[1:]

        params["pattern"] = args[0]
        i = 1
        while i < len(args):
            if args[i] in sort_aliases:
                params["sort"] = args[i+1]
                i += 1
            elif args[i] == "-f":
                params["overwrite"] = True
            else:
                if args[i][0] == "(":
                    params["files"].append(args[i][1:-1].split())
                else:
                    params["files"].append([args[i]])
            i += 1
            

        Interpreter.validate_arguments(params)
        return params