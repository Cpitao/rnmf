class Logger:
    def __init__(self):
        self.omitted_files = []
    
    def log_omitted_in_console(self):
        print("Omitted:")
        for omitted in self.omitted_files:
            print(f"{omitted[0]} as {omitted[1]}")
    
    def write_omitted_to_file(self):
        with open("rnmf_logs.txt", "w+") as f:
            f.write("\n\n")
            f.write("Omitted:\n")

            for omitted in self.omitted_files:
                f.write(f"{omitted[0]} as {omitted[1]}\n")
    
    def handle_omitted(self):
        self.log_omitted_in_console()
        print("Do you want to log omitted files? [y/n]", end=' ')
        while True:
            do_log = input()
            if do_log.lower() == "y":
                self.write_omitted_to_file()
                break
            elif do_log.lower() == "n":
                break