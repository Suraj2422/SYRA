from nlp.command_parser import CommandParser
from rpa.task_executor import TaskExecutor
from vision.screen_capture import capture_screen
from vision.ocr_engine import extract_text
from vision.activity_analyzer import ActivityAnalyzer
from rl.agent import RLAgent


class Assistant:
    def __init__(self):
        print("[INIT] SYRA initialized (Phase 2)")

        self.parser = CommandParser()
        self.executor = TaskExecutor()
        self.analyzer = ActivityAnalyzer()
        self.agent = RLAgent()

        self.active = True  # Phase 2 Step 1: always active (will change later)

    def run_once(self):
        """
        One safe execution cycle.
        Called repeatedly by main loop.
        """
        if not self.active:
            return

        try:
            user_input = input(">> ").strip()
        except EOFError:
            return

        if not user_input:
            return

        intent = self.parser.parse(user_input)
        action = intent.get("action")

        print("[INTENT]", intent)

        # EXIT (still supported)
        if action == "exit":
            print("[SHUTDOWN] SYRA exiting by command")
            raise KeyboardInterrupt

        # READ SCREEN (CV demo still valid)
        if action == "read_screen":
            frame = capture_screen()
            text = extract_text(frame)
            print("\n[SCREEN TEXT]")
            print(text[:1000])
            return

        # ANALYZE ACTIVITY (video analytics)
        if action == "analyze activity":
            frame = capture_screen()
            result = self.analyzer.analyze(frame)
            print("[ACTIVITY]", result)
            return

        # -------- RL-DRIVEN EXECUTION --------

        frame = capture_screen()
        activity_info = self.analyzer.analyze(frame)
        state = (action, activity_info["activity"])

        chosen_action = self.agent.choose_action(state)
        print("[RL] State:", state, "Chosen:", chosen_action)

        reward = 0

        if chosen_action == 0:  # execute
            try:
                if action == "open_app":
                    self.executor.open_app(intent["target"])

                elif action == "type_text":
                    self.executor.type_text(intent["content"])

                reward = 1
            except Exception as e:
                print("[ERROR]", e)
                reward = -1

        elif chosen_action == 1:
            print("[RL] Waiting (no action)")

        elif chosen_action == 2:
            print("[RL] Ignored")

        next_state = (action, activity_info["activity"])
        self.agent.update(state, chosen_action, reward, next_state)

        print("[RL] Reward:", reward)
