"""
LLM Configuration Module for Thought Leadership Crew

This module handles dynamic LLM provider configuration based on environment variables.
Supports multiple providers through CrewAI's LLM interface.

Configuration:
    - LLM_PROVIDER: The provider to use (openai, anthropic, ollama, etc.)
    - MODEL: The specific model to use
    - Provider-specific API keys as documented at https://docs.crewai.com/en/concepts/llms

The module combines LLM_PROVIDER and MODEL to create the full model string
in the format "provider/model" as required by CrewAI.

Example:
    LLM_PROVIDER=openai
    MODEL=gpt-4o
    Results in: "openai/gpt-4o"

For local models with Ollama:
    LLM_PROVIDER=ollama
    MODEL=llama3.1:8b
    Results in: "ollama/llama3.1:8b"

Supported Providers:
    - OpenAI: Requires OPENAI_API_KEY
    - Anthropic: Requires ANTHROPIC_API_KEY
    - Google Gemini: Requires GEMINI_API_KEY
    - Ollama: No API key required (runs locally)
    - Azure: Requires AZURE_API_KEY, AZURE_API_BASE, AZURE_API_VERSION
    - Mistral: Requires MISTRAL_API_KEY
    - Groq: Requires GROQ_API_KEY
    - Cohere: Requires COHERE_API_KEY

See full documentation: https://docs.crewai.com/en/concepts/llms
"""

import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    Configure and return the appropriate LLM based on environment settings.
    
    The LLM is configured using environment variables:
    - LLM_PROVIDER: The provider to use (openai, anthropic, ollama, etc.)
    - MODEL: The model name without provider prefix
    - USE_OLLAMA: If true, overrides LLM_PROVIDER to use Ollama
    
    The final model string is constructed as: {provider}/{model}
    Example: openai/gpt-4o, anthropic/claude-sonnet-4-20250514
    
    Note: API keys are automatically detected from environment variables:
    - OPENAI_API_KEY for OpenAI
    - ANTHROPIC_API_KEY for Anthropic
    No need to pass them explicitly to the LLM constructor.
    """
    # Check if Ollama is explicitly enabled (backwards compatibility)
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
    
    if use_ollama:
        # Ollama configuration - uses its own model and base URL settings
        model = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        return LLM(
            model=f"ollama/{model}",
            base_url=base_url,
            temperature=0.1
        )
    
    # Get provider and model from environment
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    model = os.getenv("MODEL", "gpt-4o")
    
    # Configuration for the LLM
    llm_config = {
        "model": f"{provider}/{model}",
        "temperature": 0.1
    }
    
    return LLM(**llm_config)