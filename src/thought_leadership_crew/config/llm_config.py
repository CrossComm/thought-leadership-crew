import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    Configure and return the appropriate LLM based on environment settings.
    """
    llm_provider = os.getenv("LLM_PROVIDER", "OPEN_AI").upper()
    
    if llm_provider == "OLLAMA":
        model = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
       
        return LLM(
            model=f"ollama/{model}",
            base_url=base_url,            
            temperature=0.1
        )
    
    elif llm_provider == "ANTHROPIC":
        model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY is required when using ANTHROPIC provider")
        
        
        return LLM(
            model=model,
            api_key=api_key,
            temperature=0.1
        )
    
    elif llm_provider == "OPEN_AI":
        model = os.getenv("OPEN_AI_MODEL", "gpt-4o")
        api_key = os.getenv("OPEN_AI_KEY")
        
        if not api_key:
            raise ValueError("OPEN_AI_KEY is required when using OPEN_AI provider")
        
        
        return LLM(
            model=f"openai/{model}",
            api_key=api_key,
            temperature=0.1
        )
    
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {llm_provider}. Must be one of: OPEN_AI, ANTHROPIC, OLLAMA")