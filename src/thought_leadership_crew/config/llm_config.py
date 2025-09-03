import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    Configure and return the appropriate LLM based on environment settings.
    """
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
    
    if use_ollama:
        model = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        return LLM(
            model=f"ollama/{model}",
            base_url=base_url,
            temperature=0.1
        )
    
    model = os.getenv("MODEL", "gpt-4o")
    
    if model.startswith("claude"):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY is required when using Claude models")
        
        return LLM(
            model=f"anthropic/{model}",
            api_key=api_key,
            temperature=0.1
        )
    
    elif model.startswith("gpt") or model.startswith("o1"):
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            raise ValueError("OPENAI_API_KEY is required when using OpenAI models")
        
        return LLM(
            model=f"openai/{model}",
            api_key=api_key,
            temperature=0.1
        )
    
    else:
        raise ValueError(f"Unsupported model: {model}. Model must start with 'claude' for Anthropic or 'gpt'/'o1' for OpenAI")