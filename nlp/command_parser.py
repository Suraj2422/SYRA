class CommandParser:
    def __init__(self):
        pass

    def parse(self, text):
        text = text.lower().strip()
        parts = text.split()

        # READ SCREEN (Computer Vision command)
        if text == "read screen":
            return {
                "action": "read_screen"
            }

        # OPEN APPLICATION
        if len(parts) >= 2 and parts[0] == "open":
            return {
                "action": "open_app",
                "target": parts[1]
            }

        # TYPE TEXT
        if parts and parts[0] == "type":
            content = " ".join(parts[1:])
            return {
                "action": "type_text",
                "content": content
            }

        # EXIT
        if text in ["exit", "quit", "stop"]:
            return {
                "action": "exit"
            }

        return {
            "action": "unknown",
            "raw": text
        }
