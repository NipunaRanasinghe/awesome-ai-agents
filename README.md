<div align="center">

<!-- title -->

<!--lint ignore no-dead-urls-->

# Awesome AI Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Lint](https://github.com/NipunaRanasinghe/awesome-ai-agents/actions/workflows/lint.yml/badge.svg)](https://github.com/NipunaRanasinghe/awesome-ai-agents/actions/workflows/lint.yml) [![Check Links](https://github.com/NipunaRanasinghe/awesome-ai-agents/actions/workflows/links.yml/badge.svg)](https://github.com/NipunaRanasinghe/awesome-ai-agents/actions/workflows/links.yml)

<!-- description -->

_A curated list of frameworks, tools, and resources for building and deploying AI agents. From multi-agent systems to autonomous coding assistants, this repository covers the latest advancements in AI agent technology._

<!-- image -->

<a href="https://github.com/NipunaRanasinghe/awesome-ai-agents" target="_blank" rel="noopener noreferrer">
  <img src="resources/images/image.png" alt="Awesome AI Agents Logo">
</a>

</div>

---

## Contents

- [🌟 Core Frameworks](#-core-frameworks)
- [🚀 Specialized Agents](#-specialized-agents)
  - [💻 Coding Agents](#-coding-agents)
  - [🔬 Research Agents](#-research-agents)
  - [🎨 Creative Agents](#-creative-agents)
  - [🌐 Web Agents](#-web-agents)
  - [🗣️ Programming Language Agents](#-programming-language-agents)
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
- [🚀 Contributors](#-contributors)

---

## 🌟 Core Frameworks

Frameworks for building and managing AI agents.

| Framework                                                                  | Stars                                                                     | Description                                                                                                              |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [AutoGen](https://github.com/microsoft/autogen)                            | ![](https://img.shields.io/github/stars/microsoft/autogen)                | Multi-agent conversations, GPT-4 integration, customizable workflows                                                     |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)                 | ![](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT)     | Autonomous AI agent for task completion, web browsing, and code execution                                                |
| [MetaGPT](https://github.com/geekan/MetaGPT)                               | ![](https://img.shields.io/github/stars/geekan/MetaGPT)                   | Simulates software company workflows, role-based agents                                                                  |
| [Neurolink](https://github.com/juspay/neurolink)                           | ![](https://img.shields.io/github/stars/juspay/neurolink)                 | Multi-provider AI agent framework, unifies 12+ LLM providers, workflow orchestration                                     |
| [CrewAI](https://github.com/joaomdmoura/crewai)                            | ![](https://img.shields.io/github/stars/joaomdmoura/crewai)               | Role-based agent orchestration, task delegation                                                                          |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI)                    | ![](https://img.shields.io/github/stars/MervinPraison/PraisonAI)          | Fastest multi-agent framework (3.77μs), 100+ LLMs, MCP, workflows, Python & JS SDKs                                      |
| [LangChain](https://github.com/langchain-ai/langchain)                     | ![](https://img.shields.io/github/stars/langchain-ai/langchain)           | Tool integration, memory management, agent chaining                                                                      |
| [LangGraph](https://github.com/langchain-ai/langgraph)                     | ![](https://img.shields.io/github/stars/langchain-ai/langgraph)           | Stateful, multi-actor applications with LLMs                                                                             |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI)                 | ![](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI)      | Open-source AGI framework, multi-modal agents                                                                            |
| [Google ADK (Agent Development Kit)](https://github.com/google/adk-python) | ![](https://img.shields.io/github/stars/google/adk-python)                | Code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents                                |
| [OpenAI Assistants API (SDK)](https://github.com/openai/openai-python)     | ![](https://img.shields.io/github/stars/openai/openai-python)             | Build AI assistants with tools and persistent threads via SDK                                                            |
| [AgentOps](https://github.com/AgentOps-AI/agentops)                        | ![](https://img.shields.io/github/stars/AgentOps-AI/agentops)             | Monitoring, cost tracking, and benchmarking SDK for agents                                                               |
| [Agentset](https://github.com/agentset-ai/agentset)                        | ![](https://img.shields.io/github/stars/agentset-ai/agentset)             | Production-ready RAG platform with agentic reasoning, hybrid search, and multimodal support                              |
| [LLMStack](https://github.com/trypromptly/LLMStack)                        | ![](https://img.shields.io/github/stars/trypromptly/LLMStack)             | No-code multi-agent framework with data workflows                                                                        |
| [Agency Swarm](https://github.com/VRSEN/agency-swarm)                      | ![](https://img.shields.io/github/stars/VRSEN/agency-swarm)               | Reliable multi-agent orchestration using OpenAI Assistants API                                                           |
| [AGiXT](https://github.com/Josh-XT/AGiXT)                                  | ![](https://img.shields.io/github/stars/Josh-XT/AGiXT)                    | Adaptive automation platform with persistent memory                                                                      |
| [Upsonic](https://github.com/upsonic/upsonic)                              | ![](https://img.shields.io/github/stars/upsonic/upsonic)                  | Reliability layer, model context protocol, task-oriented                                                                 |
| [Taskade MCP](https://github.com/taskade/mcp)                              | ![](https://img.shields.io/github/stars/taskade/mcp)                      | Open-source MCP toolkit and integrations for building AI agents and automated workflows                                  |
| [AgentVerse](https://github.com/OpenBMB/AgentVerse)                        | ![](https://img.shields.io/github/stars/OpenBMB/AgentVerse)               | Multi-agent simulation environments for research                                                                         |
| [ChatDev](https://github.com/OpenBMB/ChatDev)                              | ![](https://img.shields.io/github/stars/OpenBMB/ChatDev)                  | Collaborative software development agents                                                                                |
| [Agno](https://github.com/agno-agi/agno)                                   | ![](https://img.shields.io/github/stars/agno-agi/agno)                    | Multi-agent framework, runtime, and control plane for AI products                                                        |
| [Composio](https://github.com/ComposioHQ/composio)                         | ![](https://img.shields.io/github/stars/ComposioHQ/composio)              | 100+ integrations for AI agents via function calling, MCP compatible                                                     |
| [PocketFlow](https://github.com/The-Pocket/PocketFlow)                     | ![](https://img.shields.io/github/stars/The-Pocket/PocketFlow)            | Minimalist 100-line LLM framework for agents, workflows, and RAG                                                         |
| [CAMEL](https://github.com/camel-ai/camel)                                 | ![](https://img.shields.io/github/stars/camel-ai/camel)                   | Multi-agent framework for communicative agents research                                                                  |
| [Strands Agents SDK](https://github.com/strands-agents/sdk-python)         | ![](https://img.shields.io/github/stars/strands-agents/sdk-python)        | AWS-backed model-driven agent SDK with MCP and multi-provider support                                                    |
| [Summoner](https://github.com/Summoner-Network/summoner-agents)            | ![](https://img.shields.io/github/stars/Summoner-Network/summoner-agents) | Agent-to-agent networking for server-decoupled agents over long-lived TCP sessions (Python/Rust), 50+ runnable templates |
| [KodeAgent](https://github.com/barun-saha/kodeagent)                       | ![](https://img.shields.io/github/stars/barun-saha/kodeagent)             | The Minimal Agent Engine to build ReAct & CodeAct agents, with support for code sandbox and observability                |
| [Hivemoot Colony](https://github.com/hivemoot/colony)                      | ![](https://img.shields.io/github/stars/hivemoot/colony)                  | Self-governing multi-agent platform; agents propose, vote, peer-review, and ship software via democratic consensus       |

---

## 🚀 Specialized Agents

Agents designed for specific tasks or industries.

### 💻 Coding Agents

| Name                                                      | Stars                                                             | Description                                                             |
| --------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [SWE-agent](https://github.com/princeton-nlp/SWE-agent)   | ![](https://img.shields.io/github/stars/princeton-nlp/SWE-agent)  | AI agent for software engineering tasks                                 |
| [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot)    | ![](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot)   | Assists in writing and debugging code                                   |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands)    | ![](https://img.shields.io/github/stars/All-Hands-AI/OpenHands)   | Open-source AI software development agents (formerly OpenDevin)         |
| [Devika](https://github.com/stitionai/devika)             | ![](https://img.shields.io/github/stars/stitionai/devika)         | Agentic AI Software Engineer that writes code from natural instructions |
| [Aider](https://github.com/paul-gauthier/aider)           | ![](https://img.shields.io/github/stars/paul-gauthier/aider)      | AI pair programming in terminal                                         |
| [Plandex](https://github.com/plandex-ai/plandex)          | ![](https://img.shields.io/github/stars/plandex-ai/plandex)       | AI coding engine for complex projects                                   |
| [TaskWeaver](https://github.com/microsoft/TaskWeaver)     | ![](https://img.shields.io/github/stars/microsoft/TaskWeaver)     | Code-first agent framework for analytical tasks                         |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ![](https://img.shields.io/github/stars/google-gemini/gemini-cli) | Open-source AI agent bringing Gemini to the terminal with MCP support   |
| [AgenticSeek](https://github.com/Fosowl/agenticSeek)      | ![](https://img.shields.io/github/stars/Fosowl/agenticSeek)       | Fully local autonomous agent that browses web and codes without APIs    |

### 🔬 Research Agents

| Name                                                            | Stars                                                               | Description                                                      |
| --------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | ![](https://img.shields.io/github/stars/assafelovic/gpt-researcher) | Autonomous agent for comprehensive research                      |
| [Storm](https://github.com/stanford-oval/storm)                 | ![](https://img.shields.io/github/stars/stanford-oval/storm)        | Multi-agent system for collaborative reasoning                   |
| [DeerFlow](https://github.com/bytedance/deer-flow)              | ![](https://img.shields.io/github/stars/bytedance/deer-flow)        | Framework for deep research with web search and Python execution |

### 🎨 Creative Agents

| Name                                               | Stars                                                        | Description                             |
| -------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------- |
| [ShortGPT](https://github.com/RayVentura/ShortGPT) | ![](https://img.shields.io/github/stars/RayVentura/ShortGPT) | Short-form video generation agent       |
| [AI-town](https://github.com/a16z-infra/ai-town)   | ![](https://img.shields.io/github/stars/a16z-infra/ai-town)  | Virtual world simulation with AI agents |

### 🌐 Web Agents

| Name                                                      | Stars                                                            | Description                                                      |
| --------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| [Browser Use](https://github.com/browser-use/browser-use) | ![](https://img.shields.io/github/stars/browser-use/browser-use) | Make websites accessible for AI agents, automate tasks with ease |
| [NanoBrowser](https://github.com/nanobrowser/nanobrowser) | ![](https://img.shields.io/github/stars/nanobrowser/nanobrowser) | TypeScript-based AI browsing agent                               |
| [Firecrawl](https://github.com/firecrawl/firecrawl)       | ![](https://img.shields.io/github/stars/firecrawl/firecrawl)     | Turn websites into LLM-ready markdown or structured data         |

### 🗣️ Programming Language Agents

Agents and frameworks specialized for specific programming languages.

| Name                                                                     | Language   | Stars                                                                    | Description                                    |
| ------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------------------ | ---------------------------------------------- |
| [TypeChat](https://github.com/microsoft/TypeChat)                        | TypeScript | ![](https://img.shields.io/github/stars/microsoft/TypeChat)              | Type-safe LLM outputs using TypeScript types   |
| [LangChain.js](https://github.com/langchain-ai/langchainjs)              | JavaScript | ![](https://img.shields.io/github/stars/langchain-ai/langchainjs)        | JS version of LangChain                        |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel)          | C#/.NET    | ![](https://img.shields.io/github/stars/microsoft/semantic-kernel)       | Integrate LLMs into .NET apps                  |
| [LangChain4j](https://github.com/langchain4j/langchain4j)                | Java       | ![](https://img.shields.io/github/stars/langchain4j/langchain4j)         | Java implementation of LangChain               |
| [Haystack](https://github.com/deepset-ai/haystack)                       | Python     | ![](https://img.shields.io/github/stars/deepset-ai/haystack)             | Search and question answering agents           |
| [LlamaIndex.js](https://github.com/run-llama/LlamaIndexTS)               | TypeScript | ![](https://img.shields.io/github/stars/run-llama/LlamaIndexTS)          | JS version of LlamaIndex                       |
| [LangChain.rb](https://github.com/andreibondarev/langchainrb)            | Ruby       | ![](https://img.shields.io/github/stars/andreibondarev/langchainrb)      | Ruby implementation of LangChain               |
| [LangChainGo](https://github.com/tmc/langchaingo)                        | Go         | ![](https://img.shields.io/github/stars/tmc/langchaingo)                 | Go implementation for LLM orchestration        |
| [OpenAI Agents (Python)](https://github.com/openai/openai-agents-python) | Python     | ![](https://img.shields.io/github/stars/openai/openai-agents-python)     | Lightweight, provider-agnostic agent framework |
| [Swarms-rs](https://github.com/The-Swarm-Corporation/swarms-rs)          | Rust       | ![](https://img.shields.io/github/stars/The-Swarm-Corporation/swarms-rs) | Swarm-based agent orchestration in Rust        |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)             | JavaScript | ![](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm)      | All-in-one AI agent builder with RAG and UI    |

---

## ⚙️ Agent Operations

Tools and systems for managing AI agents.

### 🧠 Memory

| Name                                                         | Stars                                                       | Description                            |
| ------------------------------------------------------------ | ----------------------------------------------------------- | -------------------------------------- |
| [Letta (formerly MemGPT)](https://github.com/letta-ai/letta) | ![](https://img.shields.io/github/stars/letta-ai/letta)     | Dynamic, adaptive agent memory system  |
| [Mem0](https://github.com/mem0ai/mem0)                       | ![](https://img.shields.io/github/stars/mem0ai/mem0)        | Universal memory layer for AI agents   |
| [ChromaDB](https://github.com/chroma-core/chroma)            | ![](https://img.shields.io/github/stars/chroma-core/chroma) | Vector DB for memory/context           |
| [Weaviate](https://github.com/weaviate/weaviate)             | ![](https://img.shields.io/github/stars/weaviate/weaviate)  | Scalable vector DB for semantic memory |

### 📊 Evaluation

| Name                                                            | Stars                                                             | Description                                 |
| --------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| [AgentBench](https://github.com/THUDM/AgentBench)               | ![](https://img.shields.io/github/stars/THUDM/AgentBench)         | Multi-environment testing for agents        |
| [LangTrace](https://github.com/Scale3-Labs/langtrace)           | ![](https://img.shields.io/github/stars/Scale3-Labs/langtrace)    | Monitoring and trace visualization          |
| [Agent Evaluation](https://github.com/awslabs/agent-evaluation) | ![](https://img.shields.io/github/stars/awslabs/agent-evaluation) | Benchmarking agent capabilities             |
| [Simple Evals](https://github.com/openai/simple-evals)          | ![](https://img.shields.io/github/stars/openai/simple-evals)      | OpenAI's lightweight LLM evaluation library |
| [Agent OS](https://github.com/imran-siddique/agent-os)              | ![](https://img.shields.io/github/stars/imran-siddique/agent-os)      | Governance kernel for AI agents — policy enforcement, audit trails, and capability-based security |

### 🚀 Deployment

| Name                                                | Stars                                                            | Description                                  |
| --------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| [Daytona](https://github.com/daytonaio/daytona)     | ![](https://img.shields.io/github/stars/daytonaio/daytona)       | Elastic infrastructure for AI-generated code |
| [E2B](https://github.com/e2b-dev/E2B)               | ![](https://img.shields.io/github/stars/e2b-dev/E2B)             | Secure sandboxed environments for agents     |
| [OctoAI](https://github.com/octoai/octoAI)          | ![](https://img.shields.io/github/stars/octoai/octoAI)           | Scalable infrastructure for agent deployment |
| [Modal](https://github.com/modal-labs/modal-client) | ![](https://img.shields.io/github/stars/modal-labs/modal-client) | Serverless runtime for AI workloads          |

---

## 📚 Research & Benchmarks

Key research papers, benchmarks, and surveys on AI agents.

### 📄 Papers

| Title                                   | Link                                      | Description                               |
| --------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| The Rise of LLM-Based Agents            | [arXiv](https://arxiv.org/abs/2309.07864) | Comprehensive survey on LLM-based agents  |
| Tool Learning with Foundation Models    | [arXiv](https://arxiv.org/abs/2304.08354) | Tool usage in AI agents                   |
| Multi-Agent Collaboration               | [arXiv](https://arxiv.org/abs/2308.08262) | Collaboration in multi-agent systems      |
| Large Language Model based Multi-Agents | [arXiv](https://arxiv.org/abs/2312.01845) | Survey of progress and challenges         |
| Agentic AI Systems                      | [arXiv](https://arxiv.org/abs/2401.08231) | Components and applications of agentic AI |
| A Survey on LLM-based Autonomous Agents | [arXiv](https://arxiv.org/abs/2308.11432) | Focus on autonomous LLM agents            |

### 📊 Benchmarks

| Name                                                   | Stars                                                           | Description                                           |
| ------------------------------------------------------ | --------------------------------------------------------------- | ----------------------------------------------------- |
| [ToolBench](https://github.com/OpenBMB/ToolBench)      | ![](https://img.shields.io/github/stars/OpenBMB/ToolBench)      | Benchmark for tool learning                           |
| [SOTOPIA-π](https://github.com/sotopia-lab/sotopia-pi) | ![](https://img.shields.io/github/stars/sotopia-lab/sotopia-pi) | Social intelligence benchmark for multi-agent systems |

---

## 🌐 Community Resources

Join the conversation and stay updated on AI agent developments.

### 👥 Communities

| Name                | Link                                                       | Description                                          |
| ------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| LangChain Community | [Discord](https://discord.gg/langchain)                    | Active developer community                           |
| AutoGen Discussions | [GitHub](https://github.com/microsoft/autogen/discussions) | Microsoft AutoGen community forum                    |
| AgentOps Discord    | [Join](https://discord.gg/agentops)                        | Developer space for observability and testing agents |
| Letta AI Community  | [Discord](https://discord.gg/letta)                        | Discussions on adaptive memory in AI agents          |

### 📰 Newsletters

| Name                        | Link                                                | Description                                   |
| --------------------------- | --------------------------------------------------- | --------------------------------------------- |
| LangChain Newsletter        | [Subscribe](https://blog.langchain.dev/newsletter/) | LangChain and agent updates                   |
| The Batch (DeepLearning.AI) | [Subscribe](https://www.deeplearning.ai/the-batch/) | Weekly AI industry insights                   |
| Agent Weekly                | [Subscribe](https://agentweekly.com)                | News and launches from the AI agent ecosystem |

---

## 🚀 Contributors

A huge thank you to all our amazing contributors!

[![Contributors](https://contrib.rocks/image?repo=NipunaRanasinghe/awesome-ai-agents)](https://github.com/NipunaRanasinghe/awesome-ai-agents/graphs/contributors)

Your contributions make this project better every day.

⭐ A special shoutout to all our [stargazers](https://github.com/NipunaRanasinghe/awesome-ai-agents/stargazers) for your support!
**Star this repository** to stay updated and help grow the community of AI enthusiasts!

## Contributing

Your contributions are welcome! Here's how to get started:

- Fork the [repository](https://github.com/NipunaRanasinghe/awesome-ai-agents/fork) and clone it locally.
- Add your resource to the appropriate section in `README.md`.
- Ensure the resource is:
  - Relevant to AI agents.
  - Actively maintained (updated within the last 6 months).
  - Includes a brief description and link.
- Submit a pull request with a clear description of your changes.

For more details, see the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
