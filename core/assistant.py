from nlp.command_parser import CommandParser
from rpa.task_executor import TaskExecutor
from vision.screen_capture import capture_screen
from vision.ocr_engine import extract_text


class Assistant:
    def __init__(self):
        print("[INIT] SYRA initialized")
        self.parser = CommandParser()
        self.executor = TaskExecutor()

    def start(self):
        print("[START] SYRA is online. Type a command.")

        while True:
            user_input = input(">> ")
            intent = self.parser.parse(user_input)
            print("[INTENT]", intent)

            action = intent["action"]

            if action == "open_app":
                self.executor.open_app(intent["target"])

            elif action == "type_text":
                self.executor.type_text(intent["content"])

            elif action == "exit":
                print("[SHUTDOWN] SYRA shutting down.")
                break

            # 🔍 Vision demo command
            elif action == "read_screen":
                frame = capture_screen()
                text = extract_text(frame)
                print("\n[SCREEN TEXT]")
                print(text[:1000])

            else:
                print("[INFO] Command not supported.")
