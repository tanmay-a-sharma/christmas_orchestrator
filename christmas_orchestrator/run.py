"""Christmas list orchestrator that coordinates research and letter writing agents."""
from naptha_sdk.modules.orchestrator import Orchestrator
from naptha_sdk.schemas import OrchestratorRunInput

class ChristmasOrchestrator(Orchestrator):
    async def create(self, deployment, *args, **kwargs):
        """Initialize the orchestrator with agent configurations."""
        self.deployment = deployment
        
    async def run(self, module_run: OrchestratorRunInput, *args, **kwargs):
        """Execute the Christmas list workflow."""
        try:
            # Extract sender from inputs
            sender = module_run.inputs.get("sender", "Anonymous")
            
            # Step 1: Research Vuori clothing items
            print(f"Starting research for Vuori clothing...")
            research_results = await self.run_agent(
                "research_agent",
                {
                    "query": "Best Vuori clothing items for Christmas gifts 2025, focus on popular items and new releases"
                }
            )
            
            if not research_results.get("results"):
                raise Exception("Research agent did not return any results")
                
            print(f"Research complete. Writing letter to Santa...")
            # Step 2: Write letter to Santa using research results
            letter_results = await self.run_agent(
                "letter_writer_agent",
                {
                    "research_results": research_results["results"],
                    "recipient": "Santa Claus",
                    "sender": sender,
                    "tone": "polite and cheerful"
                }
            )
            
            if not letter_results.get("letter"):
                raise Exception("Letter writer agent did not generate a letter")
                
            print(f"Letter writing complete!")
            return {
                "status": "success",
                "research_results": research_results,
                "letter": letter_results["letter"]
            }
            
        except Exception as e:
            print(f"Error in Christmas orchestrator: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
