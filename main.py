from core.assistant import Assistant
import time

def main():
    assistant = Assistant()

    print("[SYSTEM] SYRA background service started")
    print("[SYSTEM] Press Ctrl+C to stop")

    try:
        while True:
            assistant.run_once()
            time.sleep(0.5)  # low CPU usage
    except KeyboardInterrupt:
        print("\n[SYSTEM] SYRA service stopped safely")

if __name__ == "__main__":
    main()
