from nlp.command_parser import CommandParser
from rpa.task_executor import TaskExecutor
from vision.screen_capture import capture_screen
from vision.ocr_engine import extract_text
from vision.activity_analyzer import ActivityAnalyzer
from rl.agent import RLAgent


class Assistant:
    def __init__(self):
        print("[INIT] SYRA initialized")

        self.parser = CommandParser()
        self.executor = TaskExecutor()
        self.analyzer = ActivityAnalyzer()
        self.agent = RLAgent()

    def start(self):
        print("[START] SYRA is online. Type a command.")

        while True:
            user_input = input(">> ")
            intent = self.parser.parse(user_input)

            action = intent["action"]
            print("[INTENT]", intent)

            # EXIT (handle early)
            if action == "exit":
                print("[SHUTDOWN] SYRA shutting down.")
                break

            # READ SCREEN (CV ONLY, NO RL)
            if action == "read_screen":
                frame = capture_screen()
                text = extract_text(frame)
                print("\n[SCREEN TEXT]")
                print(text[:1000])
                continue

            # -------- RL PIPELINE START --------

            # Capture activity for state
            frame = capture_screen()
            activity_info = self.analyzer.analyze(frame)

            state = (action, activity_info["activity"])

            # RL decision
            chosen_action = self.agent.choose_action(state)
            print("[RL] State:", state, "Chosen action:", chosen_action)

            reward = 0

            # Execute based on RL decision
            if chosen_action == 0:  # execute
                try:
                    if action == "open_app":
                        self.executor.open_app(intent["target"])

                    elif action == "type_text":
                        self.executor.type_text(intent["content"])

                    reward = 1

                except Exception as e:
                    print("[RL ERROR]", e)
                    reward = -1

            elif chosen_action == 1:  # wait
                print("[RL] Waiting before action")
                reward = 0

            elif chosen_action == 2:  # ignore
                print("[RL] Ignoring action")
                reward = 0

            # RL update
            next_state = (action, activity_info["activity"])
            self.agent.update(state, chosen_action, reward, next_state)

            print("[RL] Reward:", reward)

            # -------- RL PIPELINE END --------
