"""Christmas list orchestrator that coordinates research and letter writing agents."""
from naptha_sdk.modules.orchestrator import Orchestrator
from naptha_sdk.schemas import OrchestratorRunInput

class ChristmasOrchestrator(Orchestrator):
    async def create(self, deployment, *args, **kwargs):
        """Initialize the orchestrator with agent configurations."""
        self.deployment = deployment
        
    async def run(self, module_run: OrchestratorRunInput, *args, **kwargs):
        """Execute the Christmas list workflow."""
        # Step 1: Research Vuori clothing items
        research_results = await self.run_agent(
            "research_agent",
            {
                "query": "Vuori clothing gift ideas"
            }
        )
        
        # Step 2: Write letter to Santa using research results
        letter_results = await self.run_agent(
            "letter_writer_agent",
            {
                "research_results": research_results["results"],
                "recipient": "Santa Claus",
                "sender": "Your Name",
                "tone": "polite and cheerful"
            }
        )
        
        return {
            "status": "success",
            "research_results": research_results,
            "letter": letter_results["letter"]
        }
