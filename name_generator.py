import re
import os


class NameGenerator:
    def validate_pattern(pattern):
        special_chars = ["i", "g"]
        # special characters are preceded by \
        reserved_chars = ('<', '>', ':', '"', '/', '|', '?', '*')
        # usage of reserved characters is prohibited inside the pattern
        # \ is restricted only to special characters

        for letter in pattern:
            if letter in reserved_chars:
                print('rnmf: usage of reserved character {letter} inside the pattern')
                exit(1) 

        index_regex = r"\\i"
        if len(re.findall(index_regex, pattern)) != 1:
            print("rnmf: incorrect pattern - too many or no index specifiers")
            exit(1)
        
        group_index = r"\\g"
        if len(re.findall(group_index, pattern)) > 1:
            print("rnmf: incorrect pattern - only one group index is possible")
            exit(1)
        

    def is_name_available(new_name, file):
        if os.path.exists(new_name):
            print(f"Warning: {new_name} exists. Do you want to overwrite this file? [y/n]")
            while True:
                overwrite = input()
                if overwrite.lower() == "y":
                    return True
                if overwrite.lower() == "n":
                    print(f"Omitting {file}")
                    return False
        return True
    
    def generate_name(params):
        if params["sort"] == 'm':
            params["files"].sort(key=lambda x: os.path.getmtime(x[0]))
        elif params["sort"] == 'a':
            params["files"].sort()
        
        for i in range(len(params["files"])):
            for j in range(len(params["files"][i])):
                if len(params["files"][i]) > 1:
                    if "\\g" in new_name:
                        new_name = params["pattern"]
                            .replace("\\i", i + 1).replace("\\g", j+1)
                    else:
                        new_name = params["pattern"]
                            .replace("\\i", f"{i + 1}.{j + 1}")
                else:
                    new_name = params["pattern"]
                        .replace("\\i", str(i + 1)).replace("\\g", "")
                if NameGenerator.is_name_available(new_name, params["files"][i][j]):
                    yield params["files"][i][j], new_name
                else:
                    yield None, None
            