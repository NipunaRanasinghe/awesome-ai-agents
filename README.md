<div align="center">

<!-- title -->

<!--lint ignore no-dead-urls-->

# Awesome AI Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Check Links](https://github.com/NipunaRanasinghe/awesome-ai-agents/actions/workflows/links.yml/badge.svg)](https://github.com/NipunaRanasinghe/awesome-ai-agents/actions/workflows/links.yml)

<!-- description -->

*A curated list of frameworks, tools, and resources for building and deploying AI agents. From multi-agent systems to autonomous coding assistants, this repository covers the latest advancements in AI agent technology.*

<!-- image -->

<a href="https://github.com/NipunaRanasinghe/awesome-ai-agents" target="_blank" rel="noopener noreferrer">
  <img src="https://raw.githubusercontent.com/NipunaRanasinghe/awesome-ai-agents/main/resources/images/ai-agents-icon.png" alt="Awesome AI Agents Logo" width="256" height="256">
</a>

</div>

---

## Contents

- [🌟 Core Frameworks](#-core-frameworks)
- [🚀 Specialized Agents](#-specialized-agents)
    - [💻 Coding Agents](#-coding-agents)
    - [🔬 Research Agents](#-research-agents)
    - [🎨 Creative Agents](#-creative-agents)
    - [💻 Programming Language Agents](#-programming-language-agents)
- [⚙️ Agent Operations](#-agent-operations)
    - [🧠 Memory](#-memory)
    - [📊 Evaluation](#-evaluation)
    - [🚀 Deployment](#-deployment)
- [📚 Research & Benchmarks](#-research--benchmarks)
    - [📄 Papers](#-papers)
    - [📊 Benchmarks](#-benchmarks)
- [🌐 Community Resources](#-community-resources)
    - [👥 Communities](#-communities)
    - [📰 Newsletters](#-newsletters)

---

## 🌟 Core Frameworks

Frameworks for building and managing AI agents.

| Framework                                                  | Stars                                                                | Key Features                                                         |
|------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| [AutoGen](https://github.com/microsoft/autogen)            | ![](https://img.shields.io/github/stars/microsoft/autogen)           | Multi-agent conversations, GPT-4 integration, customizable workflows |
| [MetaGPT](https://github.com/geekan/MetaGPT)               | ![](https://img.shields.io/github/stars/geekan/MetaGPT)              | Simulates software company workflows, role-based agents              |
| [CrewAI](https://github.com/joaomdmoura/crewai)            | ![](https://img.shields.io/github/stars/joaomdmoura/crewai)          | Role-based agent orchestration, task delegation                      |
| [LangChain](https://github.com/langchain-ai/langchain)     | ![](https://img.shields.io/github/stars/langchain-ai/langchain)      | Tool integration, memory management, agent chaining                  |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | ![](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI) | Open-source AGI framework, multi-modal agents                        |
| [Upsonic](https://github.com/upsonic/upsonic)              | ![](https://img.shields.io/github/stars/upsonic/upsonic)             | Reliability layer, model context protocol, task-oriented             |
| [AgentVerse](https://github.com/OpenBMB/AgentVerse)        | ![](https://img.shields.io/github/stars/OpenBMB/AgentVerse)          | Multi-agent simulation environments for research                     |
| [ChatDev](https://github.com/OpenBMB/ChatDev)              | ![](https://img.shields.io/github/stars/OpenBMB/ChatDev)             | Collaborative agents for software development                        |
| [AGiXT](https://github.com/Josh-XT/AGiXT)                  | ![](https://img.shields.io/github/stars/Josh-XT/AGiXT)               | Advanced AI automation platform with adaptive memory                 |

---

## 🚀 Specialized Agents

Agents designed for specific tasks or industries.

### 💻 Coding Agents

| Name                                                    | Stars                                                            | Description                               |
|---------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------|
| [SWE-agent](https://github.com/princeton-nlp/SWE-agent) | ![](https://img.shields.io/github/stars/princeton-nlp/SWE-agent) | AI agent for software engineering tasks.  |
| [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot)  | ![](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot)  | Assists in writing and debugging code.    |
| [OpenDevin](https://github.com/OpenDevin/OpenDevin)     | ![](https://img.shields.io/github/stars/OpenDevin/OpenDevin)     | Open-source alternative for coding tasks. |

### 🔬 Research Agents

| Name                                                            | Stars                                                               | Description                                         |
|-----------------------------------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------|
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | ![](https://img.shields.io/github/stars/assafelovic/gpt-researcher) | Autonomous agent for comprehensive online research. |
| [Storm](https://github.com/stanford-oval/storm)                 | ![](https://img.shields.io/github/stars/stanford-oval/storm)        | Multi-agent system for collaborative research.      |

### 🎨 Creative Agents

| Name                                               | Stars                                                        | Description                                       |
|----------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------|
| [ShortGPT](https://github.com/RayVentura/ShortGPT) | ![](https://img.shields.io/github/stars/RayVentura/ShortGPT) | AI agent for generating short-form video content. |
| [AI-town](https://github.com/a16z-infra/ai-town)   | ![](https://img.shields.io/github/stars/a16z-infra/ai-town)  | Virtual world populated by AI agents.             |

## 💻 Programming Language Agents

Agents and frameworks specialized for specific programming languages.

| Name                                                            | Language   | Stars                                                               | Description                                                     |
|-----------------------------------------------------------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------|
| [TypeChat](https://github.com/microsoft/TypeChat)               | TypeScript | ![](https://img.shields.io/github/stars/microsoft/TypeChat)         | Build AI agents that use TypeScript types for structured output |
| [LangChain.js](https://github.com/langchain-ai/langchainjs)     | JavaScript | ![](https://img.shields.io/github/stars/langchain-ai/langchainjs)   | JavaScript version of LangChain for building agents             |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | C#/.NET    | ![](https://img.shields.io/github/stars/microsoft/semantic-kernel)  | SDK for integrating LLMs with C# applications                   |
| [LangChain4j](https://github.com/langchain4j/langchain4j)       | Java       | ![](https://img.shields.io/github/stars/langchain4j/langchain4j)    | Java version of LangChain for building agents                   |
| [Haystack](https://github.com/deepset-ai/haystack)              | Python     | ![](https://img.shields.io/github/stars/deepset-ai/haystack)        | Framework for building search and question answering agents     |
| [LlamaIndex.js](https://github.com/run-llama/LlamaIndexTS)      | TypeScript | ![](https://img.shields.io/github/stars/run-llama/LlamaIndexTS)     | TypeScript version of LlamaIndex for building agents            |
| [LangChain.rb](https://github.com/andreibondarev/langchainrb)   | Ruby       | ![](https://img.shields.io/github/stars/andreibondarev/langchainrb) | Ruby implementation of LangChain for building agents            |
| [LangChainGo](https://github.com/tmc/langchaingo)               | Go         | ![](https://img.shields.io/github/stars/tmc/langchaingo)            | Go implementation of LangChain for building agents              |
---

## ⚙️ Agent Operations

Tools and systems for managing AI agents.

### 🧠 Memory

| Name                                              | Stars                                                       | Description                                   |
|---------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------|
| [MemGPT](https://github.com/cpacker/MemGPT)       | ![](https://img.shields.io/github/stars/cpacker/MemGPT)     | Manages memory for LLM-based agents.          |
| [ChromaDB](https://github.com/chroma-core/chroma) | ![](https://img.shields.io/github/stars/chroma-core/chroma) | Vector database for agent memory and context. |
| [Weaviate](https://github.com/weaviate/weaviate)  | ![](https://img.shields.io/github/stars/weaviate/weaviate)  | Scalable vector database for agent memory.    |

### 📊 Evaluation

| Name                                                            | Stars                                                             | Description                                        |
|-----------------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------|
| [AgentBench](https://github.com/THUDM/AgentBench)               | ![](https://img.shields.io/github/stars/THUDM/AgentBench)         | Multi-environment testing framework for AI agents. |
| [LangTrace](https://github.com/Scale3-Labs/langtrace)           | ![](https://img.shields.io/github/stars/Scale3-Labs/langtrace)    | Monitoring and evaluation for agent workflows.     |
| [Agent Evaluation](https://github.com/awslabs/agent-evaluation) | ![](https://img.shields.io/github/stars/awslabs/agent-evaluation) | Benchmark for evaluating agent capabilities.       |

### 🚀 Deployment

| Name                                                       | Stars                                                                | Description                                      |
|------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------------|
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | ![](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI) | Deployment platform for autonomous agents.       |
| [Modal](https://github.com/modal-labs/modal-client)        | ![](https://img.shields.io/github/stars/modal-labs/modal-client)     | Serverless platform for deploying AI agents.     |

---

## 📚 Research & Benchmarks

Key research papers, benchmarks, and surveys on AI agents.

### 📄 Papers

| Title                                | Link                                      | Description                                      |
|--------------------------------------|-------------------------------------------|--------------------------------------------------|
| The Rise of LLM-Based Agents         | [arXiv](https://arxiv.org/abs/2309.07864) | Comprehensive survey on LLM-based agents.        |
| Tool Learning with Foundation Models | [arXiv](https://arxiv.org/abs/2304.08354) | Explores tool usage in AI agents.                |
| Multi-Agent Collaboration            | [arXiv](https://arxiv.org/abs/2308.08262) | Framework for collaborative multi-agent systems. |

### 📊 Benchmarks

| Name                                                            | Stars                                                             | Description                                   |
|-----------------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------|
| [AgentBench](https://github.com/THUDM/AgentBench)               | ![](https://img.shields.io/github/stars/THUDM/AgentBench)         | Evaluates agents across diverse environments. |
| [ToolBench](https://github.com/OpenBMB/ToolBench)               | ![](https://img.shields.io/github/stars/OpenBMB/ToolBench)        | Benchmark for tool learning in agents.        |

---

## 🌐 Community Resources

Join the conversation and stay updated on AI agent developments.

### 👥 Communities

| Name                         | Link                                   | Description                                   |
|------------------------------|----------------------------------------|-----------------------------------------------|
| LangChain Community          | [Discord](https://discord.gg/langchain) | Active community for LangChain and AI agents. |
| AutoGen Discussions          | [GitHub](https://github.com/microsoft/autogen/discussions) | Official discussion forum for AutoGen |

### 📰 Newsletters

| Name                 | Link                                     | Description                                           |
|----------------------|------------------------------------------|-------------------------------------------------------|
| LangChain Newsletter | [Subscribe](https://blog.langchain.dev/newsletter/) | Updates on LangChain and AI agent developments       |
| The Batch by DeepLearning.AI | [Subscribe](https://www.deeplearning.ai/the-batch/) | AI news including agent developments |

---

## 🚀 Contributors

A huge thank you to all our amazing contributors!

[![Contributors](https://contrib.rocks/image?repo=NipunaRanasinghe/awesome-ai-agents)](https://github.com/NipunaRanasinghe/awesome-ai-agents/graphs/contributors)

Your contributions make this project better every day.

⭐ A special shoutout to all our [stargazers](https://github.com/NipunaRanasinghe/awesome-ai-agents/stargazers) for your support!
**Star this repository** to stay updated and help grow the community of AI enthusiasts!

## Contributing

Your contributions are welcome! Here's how to get started:

1. **Fork the repository** and clone it locally.
2. Add your resource to the appropriate section in `README.md`.
3. Ensure the resource is:
    - Relevant to AI agents.
    - Actively maintained (updated within the last 6 months).
    - Includes a brief description and link.
4. Submit a pull request with a clear description of your changes.

For more details, see the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
