"""Research agent for finding Vuori clothing items using browser automation."""
import os
from browser_use_sdk import BrowserUseSDK
from naptha_sdk.modules.agent import Agent
from naptha_sdk.schemas import AgentRunInput

class ResearchAgent(Agent):
    async def create(self, deployment, *args, **kwargs):
        """Initialize the research agent with browser SDK."""
        self.deployment = deployment
        self.sdk = BrowserUseSDK(
            chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        )
        
    async def run(self, module_run: AgentRunInput, *args, **kwargs):
        """Execute research task using browser automation."""
        # Extract inputs
        query = module_run.inputs.get("query", "")
        
        # Use our SDK to automate browser research
        results = await self.sdk.search_and_extract(
            url="https://vuoriclothing.com",
            search_query=query,
            extraction_fields=["name", "price", "description"]
        )
        
        return {
            "status": "success",
            "results": results
        }
