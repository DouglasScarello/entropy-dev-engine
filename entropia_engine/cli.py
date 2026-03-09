import sys
from .core.orchestrator import Orchestrator

def main():
    if len(sys.argv) < 2:
        print("Usage: entropia [command] [args]")
        return

    command = sys.argv[1]
    
    if command == "run":
        idea = sys.argv[2] if len(sys.argv) > 2 else "New Project"
        print(f"🚀 Starting Entropy Dev Engine for idea: '{idea}'")
        orchestrator = Orchestrator()
        orchestrator.start_debate(idea)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
