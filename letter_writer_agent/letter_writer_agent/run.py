"""Letter writer agent for creating Christmas letters using browser automation."""
import os
from browser_use_sdk import BrowserUseSDK
from naptha_sdk.modules.agent import Agent
from naptha_sdk.schemas import AgentRunInput

class LetterWriterAgent(Agent):
    async def create(self, deployment, *args, **kwargs):
        """Initialize the letter writer agent with browser SDK."""
        self.deployment = deployment
        self.sdk = BrowserUseSDK(
            chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        )
        
    async def run(self, module_run: AgentRunInput, *args, **kwargs):
        """Write and save a Christmas letter using browser automation."""
        # Extract inputs
        research_results = module_run.inputs.get("research_results", [])
        
        # Format the letter content
        letter_content = "Dear Santa,\n\n"
        for item in research_results:
            letter_content += f"I would love to receive the {item['name']} ({item['price']}).\n"
            letter_content += f"It's amazing because {item['description']}\n\n"
        letter_content += "\nThank you Santa!\nBest wishes"
        
        # Use our SDK to save to Google Drive
        saved_file = await self.sdk.save_to_google_drive(
            content=letter_content,
            filename="Christmas_List_2025.txt",
            folder="Christmas"
        )
        
        return {
            "status": "success",
            "saved_file": saved_file
        }
