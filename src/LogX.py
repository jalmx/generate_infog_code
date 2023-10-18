class BCOLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKGREEN_BG = '\033[42m'
    WARNING = '\033[93m'
    ERROR = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Log:

    @staticmethod
    def i(*message, debug=True):
        if debug:
            print(f"{BCOLORS.OKGREEN_BG} Info: {BCOLORS.ENDC}{BCOLORS.OKGREEN}[", end="")
            print(*message, end="")
            print(f"]{BCOLORS.ENDC}")

    @staticmethod
    def e(*message, debug=True):
        long_spacer = 120
        if debug:
            print(f"{BCOLORS.ERROR}[{'=' * long_spacer}]")
            print("Error: ", *message)
            print(f"[{'=' * long_spacer}]{BCOLORS.ENDC}")


if __name__ == "__main__":
    Log.e("hola", "mensajes", "mas texto")
