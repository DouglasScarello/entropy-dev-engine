from ..agents.creator import CreatorAgent
from ..agents.critic import CriticAgent
from ..agents.judge import JudgeAgent
from ..output.writer import OutputWriter

class Orchestrator:
    def __init__(self):
        self.creator = CreatorAgent()
        self.critic = CriticAgent()
        self.judge = JudgeAgent()
        self.writer = OutputWriter()

    def start_debate(self, idea: str):
        print(f"[Orchestrator] Initiating debate loop for: {idea}")
        
        # Simulated loop
        for round in range(1, 4):
            print(f"\n--- Round {round} ---")
            self.creator.design(idea)
            self.critic.review({})
            
            if self.judge.decide([]):
                print("\n✅ Architecture approved by Judge.")
                self.writer.write(idea.replace(" ", "_").lower(), {})
                break
