class CommandParser:
    def __init__(self):
        pass

    def parse(self, text):
        text = text.lower().strip()

        # OPEN APPLICATION
        if text.startswith("open"):
            parts = text.split(" ")
            if len(parts) >= 2:
                return {
                    "action": "open_app",
                    "target": parts[1]
                }

        # SEARCH QUERY
        if text.startswith("search"):
            query = text.replace("search", "").strip()
            return {
                "action": "search",
                "query": query
            }

        # TYPE TEXT
        if text.startswith("type"):
            content = text.replace("type", "").strip()
            return {
                "action": "type_text",
                "content": content
            }

        # EXIT ASSISTANT
        if text in ["exit", "quit", "stop"]:
            return {
                "action": "exit"
            }

        # UNKNOWN COMMAND
        return {
            "action": "unknown",
            "raw": text
        }
