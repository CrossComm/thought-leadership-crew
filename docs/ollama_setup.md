# Setting Up Ollama for Local LLM Usage

## Prerequisites
1. Install Ollama from [ollama.ai](https://ollama.ai/)
2. Verify installation: `ollama --version`

## Setup Steps

### 1. Pull a Model
```bash
# Pull the default llama3 model
ollama pull llama3

# Or pull a specific variant
ollama pull llama3:70b

# For smaller models, you can also use:
ollama pull phi
ollama pull mistral
```

### 2. Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env`:
```env
# Enable Ollama
USE_OLLAMA_LOCALLY=true

# Configure model (matches what you pulled)
OLLAMA_MODEL=llama3:latest

# Ollama server URL (default)
OLLAMA_BASE_URL=http://localhost:11434
```

### 3. Verify Ollama is Running
```bash
# Start Ollama if not already running
ollama serve

# In another terminal, test the model
ollama run llama3 "Hello, world!"
```

### 4. Run CrewAI with Ollama
```bash
# Run as usual
uv run src/thought_leadership_crew/main.py run
```

## Switching Between Local and Cloud LLMs
Simply toggle `USE_OLLAMA_LOCALLY` in your `.env` file:
- `true` - Uses Ollama locally
- `false` - Uses OpenAI/Anthropic (requires API keys)

## Available Models
Some popular models you can use with Ollama:
- `llama3` - Meta's latest Llama model
- `llama3:70b` - Larger variant for better performance
- `mistral` - Fast and efficient model
- `phi` - Microsoft's small language model
- `codellama` - Specialized for code generation

## Performance Tips
1. **Model Selection**: Choose smaller models (7B parameters) for faster responses on consumer hardware
2. **Memory**: Ensure you have enough RAM (8GB minimum for 7B models, 32GB+ for 70B models)
3. **GPU**: Ollama can use NVIDIA GPUs for acceleration if available

## Troubleshooting

### Ollama not responding
- Ensure Ollama service is running: `ollama serve`
- Check if the port is in use: `netstat -an | findstr 11434` (Windows) or `lsof -i :11434` (Mac/Linux)

### Model not found
- Check available models: `ollama list`
- Pull the model if missing: `ollama pull <model-name>`

### Out of memory errors
- Try a smaller model variant
- Close other applications to free up RAM
- Consider using quantized versions (e.g., `llama3:7b-q4_0`)

### Slow performance
- Use a smaller model
- Ensure no other heavy processes are running
- Consider using GPU acceleration if available

## Windows-Specific Notes
On Windows, you may need to:
1. Run Ollama as Administrator for first-time setup
2. Allow Ollama through Windows Firewall
3. Use PowerShell or Command Prompt to run Ollama commands