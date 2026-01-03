from core.assistant import Assistant
import time

def main():
    assistant = Assistant()

    print("[SYSTEM] SYRA service running (Dormant by default)")
    print("[SYSTEM] Type 'syra' to activate, 'go to sleep' to deactivate")
    print("[SYSTEM] Ctrl+C to stop\n")

    try:
        while True:
            assistant.run_once()
            time.sleep(0.3)  # very low CPU
    except KeyboardInterrupt:
        print("\n[SYSTEM] SYRA stopped safely")

if __name__ == "__main__":
    main()
