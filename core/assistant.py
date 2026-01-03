from nlp.command_parser import CommandParser


class Assistant:
    def __init__(self):
        print("[INIT] SYRA initialized")
        self.parser = CommandParser()

    def start(self):
        print("[START] SYRA is online. Type a command.")

        while True:
            user_input = input(">> ")

            intent = self.parser.parse(user_input)
            print("[INTENT]", intent)

            if intent["action"] == "exit":
                print("[SHUTDOWN] SYRA shutting down.")
                break
