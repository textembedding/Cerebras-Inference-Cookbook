# AI Agents with Cerebras Inference

This document provides an overview of the AI agents and multi-agent systems included in the Cerebras Inference Cookbook. These examples demonstrate how to leverage Cerebras' ultra-fast inference capabilities to build intelligent, interactive agent pipelines.

## 🤖 Featured Agent Systems

### Multi-Agent Pipelines

#### [Search-Based Report Generation Agent](./agents/search-agent)
**Location**: `agents/search-agent/`  
**Guide**: [Cookbook Documentation](https://inference-docs.cerebras.ai/cookbook/search-agent)

A sophisticated multi-agent system that automatically generates comprehensive research reports from web sources. The system follows a structured 5-phase pipeline:

- **User Interaction**: Collects topics and clarifying questions
- **Research & Summarization**: Generates targeted queries and article summaries
- **Report Outlining**: Synthesizes research into structured outlines
- **Report Writing**: Converts outlines to full-length reports
- **Citation Management**: Formats citations for polished final output

**Key Components**:
- Interactor: Refines user topics through clarifying questions
- Researcher: Conducts web searches and summarizes articles
- Outliner: Creates structured report frameworks
- Writer: Generates comprehensive written content
- Citer: Manages proper citation formatting

#### [Gist Memory ReadAgent](./agents/gist-memory)
**Location**: `agents/gist-memory/`  
**Guide**: [Cookbook Documentation](https://inference-docs.cerebras.ai/cookbook/gist-memory)

An intelligent document processing system that implements [Gist Memory](https://arxiv.org/abs/2402.09727) for efficient question-answering on long documents. Inspired by Google DeepMind's research, this agent processes lengthy papers into digestible "gists" and intelligently retrieves specific sections when answering questions.

**Pipeline**:
- **Document Ingestion**: Converts ArXiv papers from PDF to HTML
- **Intelligent Pagination**: Identifies natural document break points
- **Hierarchical Summarization**: Creates compressed "gist" representations
- **Selective Memory Retrieval**: Identifies relevant sections for questions
- **Context-Aware Response**: Expands gists to full text for accurate answers

**Key Components**:
- GistAgent: Core orchestrator for processing and Q&A
- ArXiv Parser: Handles PDF to HTML conversion
- Memory System: Manages hierarchical document representations

### Interactive Notebook Examples

#### [Build Your Own Perplexity](./agents/build-your-own-perplexity.ipynb)
A step-by-step guide to creating a search-powered AI assistant similar to Perplexity. Demonstrates real-time web search integration with conversational AI.

#### [Automated User Research](./agents/automate-user-research.ipynb)
An agent system for conducting automated user research, including survey design, data collection, and analysis.

#### [LiveKit Sales Agent](./agents/sales-agent-cerebras-livekit.ipynb)
A voice-enabled sales agent built with LiveKit and Cerebras Inference, demonstrating real-time conversational AI capabilities.

#### [LiveKit Interviewer](./agents/livekit_interviewer.ipynb)
An AI interviewer system using LiveKit for conducting structured interviews with natural conversation flow.

## 🚀 Getting Started

### Prerequisites

1. **Cerebras API Access**: Get your API key from [Cerebras Cloud](https://cloud.cerebras.ai)
2. **Environment Setup**: Set your API key as an environment variable:
   ```bash
   export CEREBRAS_API_KEY=<your API key>
   ```

### Running the Examples

Each agent system includes detailed setup instructions in its respective directory. Most examples are provided as:

- **Standalone Projects**: Complete implementations with `src/` directories
- **Jupyter Notebooks**: Interactive tutorials and demonstrations
- **Documentation**: Comprehensive guides linked to the [Cerebras Cookbook](https://inference-docs.cerebras.ai/cookbook)

### Quick Start Commands

```bash
# Clone the repository
git clone https://github.com/cerebras/Cerebras-Inference-Cookbook.git
cd Cerebras-Inference-Cookbook

# Navigate to a specific agent
cd agents/search-agent
# or
cd agents/gist-memory

# Follow the setup instructions in each README.md
```

## 🏗️ Architecture Patterns

### Common Design Patterns

1. **Modular Agent Architecture**: Each agent has specialized responsibilities
2. **Pipeline-Based Processing**: Multi-stage workflows for complex tasks
3. **Memory Management**: Intelligent storage and retrieval of context
4. **Citation & Sources**: Proper attribution and fact-checking
5. **Interactive Refinement**: Iterative improvement through user feedback

### Performance Optimization

- **Ultra-Fast Inference**: Leverage Cerebras' low-latency capabilities
- **Batch Processing**: Optimize multiple requests for efficiency
- **Streaming Responses**: Real-time output for better user experience
- **Selective Context**: Intelligent context window management

## 📚 Additional Resources

- **[Cerebras Inference Documentation](https://inference-docs.cerebras.ai)**: Complete API reference and guides
- **[Cookbook Site](https://inference-docs.cerebras.ai/cookbook)**: Detailed walkthroughs for each example
- **[Production Tips](https://inference-docs.cerebras.ai/production)**: Best practices for deployment

## 🤝 Contributing

These examples are designed to be educational and extensible. Feel free to:

- Modify agents for your specific use cases
- Combine patterns from different examples
- Share improvements and optimizations
- Report issues or suggest new agent patterns

## 📄 License

See the main repository [LICENSE](./LICENSE) for license information.

---

**Note**: These examples showcase the power of fast inference for agent applications. The low-latency capabilities of Cerebras Inference enable more interactive, iterative, and responsive AI agents compared to traditional inference providers.