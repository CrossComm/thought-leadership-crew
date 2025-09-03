# Changelog

All notable changes to the Thought Leadership Crew project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-09-03

### Added
- Initial release of Thought Leadership Crew
- Multi-agent system for strategic intelligence gathering
- News collection from configurable trusted sources
- Strategic analysis with role-based relevance ranking
- Executive digest generation with fact-checking
- Social media content creation for multiple platforms
- Support for multiple LLM providers (OpenAI, Anthropic, Ollama, etc.)
- Customizable user preferences and objectives
- Date-aware news filtering
- Comprehensive documentation and setup guides

### Features
- **News Collector Agent**: Automated article extraction with source monitoring
- **Strategic Analyst Agent**: Multi-criteria decision analysis for relevance scoring
- **Digest Creator Agent**: Executive briefing synthesis with verification
- **Editorial Publisher Agent**: Platform-optimized social media content generation

### Technical
- Built on CrewAI framework v0.165.0+
- Python 3.10-3.14 compatibility
- UV dependency management
- Environment-based configuration
- Extensible tool architecture
- Parallel task execution for improved performance
- JSON-structured output with Pydantic models

### Outputs
- `executive_digest.md` - Strategic intelligence briefing
- `social_media_posts.md` - Ready-to-post social content
- `final_deliverables.md` - Combined output document
- JSON analysis files for transparency and debugging