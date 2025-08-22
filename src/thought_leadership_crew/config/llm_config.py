import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    Configure and return the appropriate LLM based on environment settings.
    """
    use_ollama = os.getenv("USE_OLLAMA_LOCALLY", "false").lower() == "true"
    
    if use_ollama:
        # Configure Ollama for local usage
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3:latest")
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        return LLM(
            model=f"ollama/{ollama_model}",
            base_url=ollama_base_url
        )
    else:
        # Use default OpenAI/Anthropic configuration
        # CrewAI will use OPENAI_API_KEY from environment automatically
        model = os.getenv("MODEL", "gpt-4")
        return LLM(model=model)