class Log:

    @staticmethod
    def i(*message, debug=True):
        if debug:
            print("Info: [", *message, "]")

    @staticmethod
    def e(*message, debug=True):
        long_spacer = 80
        if debug:
            print("=" * long_spacer)
            print("Error", *message)
            print("=" * long_spacer)


if __name__ == "__main__":
    Log.e("hola", "mensajes", "mas texto")
