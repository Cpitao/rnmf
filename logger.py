class Logger:
    def __init__(self):
        omitted_files = []
    
    def log_omitted_in_console(self):
        print("Omitted:")
        for omitted in self.omitted_files:
            print(omitted[0] as omitted[1])
    
    def write_omitted_to_file(self):
        with open("rnmf_logs.txt", "a+") as f:
            f.write("\n\n")
            for omitted in self.omitted_files:
                f.write("Omitted:\n")
                f.write(f"{omitted[0]} as {omitted[1]}\n")
    
    def handle_omitted(self):
        log_omitted_in_console(self)
        print("Do you want to log omitted files? [y/n]")
        while True:
            do_log = input()
                if do_log.lower() == "y":
                    write_omitted_to_file(self)
                    break
                elif do_log.lower() == "n":
                    break